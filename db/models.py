from sqlalchemy import Table, Column, Integer, String

from sqlalchemy.orm import Mapped ,mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Child(Base):
    __tablename__ = "children"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    surname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(50))
    groupa: Mapped[str] = mapped_column(String(50))