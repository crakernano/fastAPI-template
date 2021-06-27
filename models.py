from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from database import Base


class myModel(Base):
    __tablename__ = "myTable"
    id = Column(Integer, primary_key=True, index=True)
