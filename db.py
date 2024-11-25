import os

from models import Child

import sqlalchemy


engine = sqlalchemy.create_engine("sqlite:///DOUTEST.db")
metadata = sqlalchemy.MetaData()
children_table = sqlalchemy.Table(
    "children",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("surname", sqlalchemy.String),
    sqlalchemy.Column("lastname", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.Integer),
    sqlalchemy.Column("gender", sqlalchemy.String),
    sqlalchemy.Column("groupa", sqlalchemy.String),
)

metadata.create_all(engine)

def add_child(model: Child):
    with engine.connect() as conn:
        conn.execute(children_table.insert().values(name=model.name, surname=model.surname, lastname=model.lastname, age=model.age, gender=model.gender, groupa=model.groupa))
        conn.commit()


def print_children():
    with engine.connect() as conn:
        children_list = conn.execute(children_table.select()).fetchall()
        return [Child(name=row[1], surname=row[2], lastname=row[3], age=row[4], gender=row[5], groupa=row[6]) for row in children_list]

def get_child_by_id(id) -> Child:
    with engine.connect() as conn:
        try:
            child = conn.execute(children_table.select().where(children_table.c.id == id)).fetchone()
            return Child(name=child[1], surname=child[2], lastname=child[3], age=child[4], gender=child[5], groupa=child[6])
        except




        

def main():
    add_child(Child(name="John", surname="Doe", lastname="Smith", age=12, gender="male", groupa="groupa1"))
    add_child(Child(name="Jane", surname="Doe", lastname="Smith", age=12, gender="female", groupa="groupa1"))
    add_child(Child(name="Jack", surname="mike", lastname="biden", age=12, gender="male", groupa="groupa1"))
    print_children()

if __name__ == "__main__":
    main()