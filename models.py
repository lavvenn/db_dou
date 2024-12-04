import datetime
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
    birthday: str # d/m/y
    groupa: str

class RavenTest(BaseModel):

    child_id:int

    a_1:int
    a_2:int
    a_3:int
    a_4:int
    a_5:int
    a_6:int
    a_7:int
    a_8:int
    a_9:int
    a_10:int
    a_11:int
    a_12:int

    ab_1:int
    ab_2:int
    ab_3:int
    ab_4:int
    ab_5:int
    ab_6:int
    ab_7:int
    ab_8:int
    ab_9:int
    ab_10:int
    ab_11:int
    ab_12:int

    b_1:int
    b_2:int
    b_3:int
    b_4:int
    b_5:int
    b_6:int
    b_7:int
    b_8:int
    b_9:int
    b_10:int
    b_11:int
    b_12:int


class EmotionTest(BaseModel):
    child_id:int

    e_1:str
    e_2:str
    e_3:str
    e_4:str
    e_5:str
    e_6:str

class RelationTest(BaseModel):
    child_id:int

    r_1:int
    r_2:int
    r_3:int 
    r_4:int
    r_5:int
    r_6:int
    r_7:int
    r_8:int
    r_9:int
    r_10:int
    r_11:int
    r_12:int
    r_13:int
    r_14:int
    r_15:int
    r_16:int
    r_17:int
    r_18:int
    r_19:int



