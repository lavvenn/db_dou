import datetime

from sqlalchemy import select

from db.data_baze import Session, engine, Base
from db.models import Child_ORM, EmotionTest_ORM, RavenTest_ORM, RelationTest_ORM
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
    try:
        with Session() as session:
            child = session.get(Child_ORM, id)
            return Child(name=child.name, surname=child.surname, lastname=child.lastname, birthday=child.birthday, groupa=child.groupa)
    except:
        return "child not found"
        
            
def remove_child_by_id(id):
    try:
        with Session() as session:
            child = session.get(Child_ORM, id)
            session.delete(child)
            session.commit()
        
        return "child {id} was deleted"
    except:
        return "child not found"


def raven_test_by_child_id(child_id):
    with Session() as session:
        raven_test = session.execute(select(RavenTest_ORM).where(RavenTest_ORM.child == child_id)).scalars().all()
        return raven_test


def emotion_test_by_child_id(child_id):
    with Session() as session:
        emotion_test = session.execute(select(EmotionTest_ORM).where(EmotionTest_ORM.child == child_id)).scalars().all()
        return emotion_test


def relation_test_by_child_id(child_id):
    with Session() as session:
        relation_test = session.execute(select(RelationTest_ORM).where(RelationTest_ORM.child == child_id)).scalars().all()
        return relation_test


def all_raven_tests():
    with Session() as session:
        raven_tests = session.execute(select(RavenTest_ORM)).scalars().all()
        return raven_tests

def all_emotion_tests():
    with Session() as session:
        emotion_tests = session.execute(select(EmotionTest_ORM)).scalars().all()
        return emotion_tests

def all_relation_tests():
    with Session() as session:
        relation_tests = session.execute(select(RelationTest_ORM)).scalars().all()
        return relation_tests

    
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
        child_id (int): The ID of the child to associate the test result with.

    """
    with Session() as session:
        emotion_test = EmotionTest_ORM(result=result_dict["sum"],
                                       child=child_id,
                                       added_at=datetime.datetime.now())
        session.add(emotion_test)
        session.commit()

    return "result of emotion test was added"

def add_relation_test(result_dict: dict[str, int], child_id: int):
    """
    Add a new relation test result to the database for a specific child.

    Args:
        result_dict (dict[str, int]): A dictionary containing the results of the relation test,
        child_id (int): The ID of the child to associate the test result with.

    """
    with Session() as session:
        relation_test = RelationTest_ORM(result=result_dict["sum"],
                                         child=child_id,
                                         added_at=datetime.datetime.now())
        session.add(relation_test)
        session.commit()

    return "result of relation test was added"