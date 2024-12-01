import datetime

from sqlalchemy import select

from db.data_baze import Session, engine, Base
from db.models import Child_ORM, EmotionTest_ORM, RavenTest_ORM
from models import Child

def create_all_tables():
    Base.metadata.create_all(engine)


def add_child(model: Child):
    with Session() as session:
        child = Child_ORM(name=model.name,
                           surname=model.surname,
                           lastname=model.lastname, 
                           birthday=datetime.datetime.strptime(model.birthday, "%d/%m/%Y"), 
                           groupa=model.groupa, 
                           added_at=datetime.datetime.now(), 
                           updated_at=None)
        session.add(child)
        session.commit()
    return f"child {model.name}was added"


def all_children():
    with Session() as session:
        children = session.execute(select(Child_ORM)).scalars().all()
        return children
    
def child_by_id(id) -> Child_ORM:
    with Session() as session:
        child = session.get(Child_ORM, id)
        return Child(name=child.name, surname=child.surname, lastname=child.lastname, birthday=child.birthday, groupa=child.groupa)
    
def remove_child_by_id(id):
    with Session() as session:
        child = session.get(Child_ORM, id)
        session.delete(child)
        session.commit()
    
    return "child {id} was deleted"
    
def add_raven_test(result_dict: dict[str, int], child_id: int):
    """
    Add a new Raven test result to the database for a specific child.

    Args:
        result_dict (dict[str, int]): A dictionary containing the results of the Raven test,
                                      with keys "a", "ab", "b" representing different result categories.
        child_id (int): The ID of the child to associate the test result with.

    """
    with Session() as session:
        raven_test = RavenTest_ORM(result_a=result_dict["a"],
                                   result_ab=result_dict["ab"],
                                   result_b=result_dict["b"],
                                   result_sum=result_dict["sum"],
                                   child=child_id,
                                   added_at=datetime.datetime.now())
        session.add(raven_test)
        session.commit()

    return "result of raven test was added"

def add_emotion_test(result_dict: dict[str, int], child_id: int):
    """
    Add a new emotion test result to the database for a specific child.

    Args:
        result_dict (dict[str, int]): A dictionary containing the results of the emotion test,
                                      with keys "a", "ab", "b" representing different result categories.
        child_id (int): The ID of the child to associate the test result with.

    """
    with Session() as session:
        emotion_test = EmotionTest_ORM(result=result_dict["sum"],
                                       child=child_id,
                                       added_at=datetime.datetime.now())
        session.add(emotion_test)
        session.commit()

    return "result of emotion test was added"