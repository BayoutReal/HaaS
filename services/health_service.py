from sqlalchemy.orm import Session
from models.health_data import HealthData
from schemas.health_data import HealthDataCreate

class HealthService:
    def __init__(self, db: Session):
        self.db = db

    def create_health_data(self, health_data: HealthDataCreate):
        db_health_data = HealthData(**health_data.dict())
        self.db.add(db_health_data)
        self.db.commit()
        self.db.refresh(db_health_data)
        return db_health_data

    def get_health_data(self, user_id: int, skip: int = 0, limit: int = 100):
        return self.db.query(HealthData).filter(HealthData.user_id == user_id).offset(skip).limit(limit).all()
