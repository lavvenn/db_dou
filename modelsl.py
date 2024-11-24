from pydantic import BaseModel


# def create_db():
#     if not os.path.exists("DOUTEST.db"):
#         db = sqlite3.connect("DOUTEST.db")
#         cursor = db.cursor()
#         cursor.execute("""

#         CREATE TABLE IF NOT EXISTS cildren (
#             id integer PRIMARY KEY AUTOINCREMENT,
#             name text NOT NULL,
#             surname text NOT NULL,
#             lastname text NOT NULL,
#             age int NOT NULL,
#             gender text NOT NULL,
#             groupa text NOT NULL
#         )
#         """)
#         db.commit()

class Child(BaseModel):
    name: str
    surname: str
    lastname: str
    age: int
    gender: str
    groupa: str