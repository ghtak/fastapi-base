from sqlalchemy import (
    Integer,
    String,
    Column
)
from entities.base import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user_table'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    images = relationship(
        'UserImage', back_populates="user")
