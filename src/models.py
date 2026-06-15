from sqlalchemy import Integer, String, Column
from database import Base


class Student(Base):

    __tablename__ = "students"

    id=Column(Integer, primary_key=True )
    name=Column(String)
    age=Column(Integer)
    email=Column(String)

