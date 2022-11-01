from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    LargeBinary
)
from entities.base import Base
from sqlalchemy.orm import relationship


class UserImage(Base):
    __tablename__ = 'user_image_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(LargeBinary)
    user_id = Column(Integer, ForeignKey('user_table.id'))
    user = relationship(
        "User", back_populates="images")
