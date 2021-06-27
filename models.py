from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from database import Base


class myModel(Base):
    __tablename__ = "myTable"
    __table_args__ = {'extend_existing': True}
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
