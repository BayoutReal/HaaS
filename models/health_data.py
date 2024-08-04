# models/health_data.py
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class HealthData(Base):
    __tablename__ = 'health_data'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    steps = Column(Integer)
    heart_rate = Column(Float)
    calories_burned = Column(Float)
    sleep_hours = Column(Float)
    timestamp = Column(DateTime)

    user = relationship("User", back_populates="health_data")
