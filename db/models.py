from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.data_baze import Base


class Child_ORM(Base):
    __tablename__ = "cildren"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] 
    surname: Mapped[str] 
    lastname: Mapped[str] 
    birthday: Mapped[int]
    groupa: Mapped[str]
    added_at: Mapped[int]
    updated_at: Mapped[int|None]

class RavenTest_ORM(Base):

    __tablename__ = "raven_test"      
 
    id: Mapped[int] = mapped_column(primary_key=True)
    result_a: Mapped[int]
    result_ab: Mapped[int]
    result_b: Mapped[int]
    result_sum: Mapped[int]
    child: Mapped[int] = mapped_column(ForeignKey("cildren.id"))
    added_at: Mapped[int]

class EmotionTest_ORM(Base):

    __tablename__ = "emotion_test"

    id: Mapped[int] = mapped_column(primary_key=True)
    result: Mapped[int]
    child: Mapped[int] = mapped_column(ForeignKey("cildren.id"))
    added_at: Mapped[int]