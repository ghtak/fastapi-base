from sqlalchemy import (
    Integer,
    String,
    Column
)
from entities.base import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
