from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Users(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)

    comments = relationship("Comments", back_populates="user")
