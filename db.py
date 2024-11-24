import sqlite3
import os

def create_db():
    if not os.path.exists("DOUTEST.db"):
        db = sqlite3.connect("DOUTEST.db")
        cursor = db.cursor()
        cursor.execute("""

        CREATE TABLE IF NOT EXISTS cildren (
            id integer PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            surname text NOT NULL,
            lastname text NOT NULL,
            age int NOT NULL,
            gender text NOT NULL,
            groupa text NOT NULL
        )
        """)
        db.commit()

def add_child(name: str, surname: str, lastname: str, age: int, gender: str, groupa: str):
    db = sqlite3.connect("DOUTEST.db")
    cursor = db.cursor()
    cursor.execute("""
    INSERT INTO cildren (name, surname, lastname, age, gender, groupa) VALUES (?, ?, ?, ?, ?, ?)
    """, (name, surname, lastname, age, gender, groupa))
    db.commit()

def add_groupa_table(groupa: str):
    db = sqlite3.connect("DOUTEST.db")
    cursor = db.cursor()
    cursor.execute("""
    INSERT INTO cildren (groupa) VALUES (?)
    """, (groupa,))
    db.commit()

def print_children():
    db = sqlite3.connect("DOUTEST.db")
    cursor = db.cursor()
    cursor.execute("""
    SELECT * FROM cildren
    """)
    return cursor.fetchall()

        

def main():
    create_db()
    add_child("john", "doe", "smith", 12, "male", "groupa1")
    add_child("jane", "doe", "smith", 12, "female", "groupa1")
    add_child("jane", "doe", "smith", 12, "female", "groupa2")
    print_children()

if __name__ == "__main__":
    main()