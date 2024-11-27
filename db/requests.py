import datetime

from sqlalchemy import select

from db.data_baze import Session, engine, Base
from db.models import Child_ORM
from models import Child

def create_all_tables():
    Base.metadata.create_all(engine)


def get_all_children():
    with Session() as session:
        children = session.execute(select(Child_ORM)).scalars().all()
        return [Child(name=row.name, surname=row.surname, lastname=row.lastname, birthday=row.birthday, groupa=row.groupa) for row in children]


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


def get_all_children():
    with Session() as session:
        children = session.execute(select(Child_ORM)).scalars().all()
        return children
    
def get_child_by_id(id) -> Child_ORM:
    with Session() as session:
        child = session.get(Child_ORM, id)
        return Child(name=child.name, surname=child.surname, lastname=child.lastname, birthday=child.birthday, groupa=child.groupa)