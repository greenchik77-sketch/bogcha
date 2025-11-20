from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    kindergarten_id = Column(Integer, ForeignKey("kindergartens.id"), nullable=False)
    comment = Column(String(255), nullable=False)
    rating = Column(Integer, nullable=False)

    user = relationship("Users", back_populates="comments")
    kindergarten = relationship("Kindergartens", back_populates="comments")