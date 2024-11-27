# from sqlalchemy import Column, Integer, String
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