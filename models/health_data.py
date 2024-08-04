from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class HealthData(Base):
    __tablename__ = 'health_data'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    steps = Column(Integer)
    sleep_hours = Column(Float)

    user = relationship("User", back_populates="health_data")
