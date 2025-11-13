from sqlalchemy import Column, Integer, String, Float, JSON, Text, Time, Boolean
from database import Base


class Kindergartens(Base):

    __tablename__ = "kindergartens"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    region = Column(String(255), nullable=False)
    district = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    programs = Column(JSON, nullable=False)
    languages = Column(JSON, nullable=False)
    price = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    image = Column(String(255), nullable=False)
    short = Column(Text, nullable=False)
    phone_number = Column(String(255), nullable=False)
    capacity = Column(Integer, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    age_limit = Column(String(255), nullable=False)
    islaw = Column(Boolean, nullable=False)
    mini_gallery = Column(JSON, nullable=False)
