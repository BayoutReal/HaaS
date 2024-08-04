from sqlalchemy.orm import Session
from models.health_data import HealthData
from schemas.health_data import HealthDataCreate

class HealthService:
    def __init__(self, db: Session):
        self.db = db

    def create_health_data(self, health_data: HealthDataCreate):
        db_health_data = HealthData(user_id=health_data.user_id, steps=health_data.steps, sleep_hours=health_data.sleep_hours)
        self.db.add(db_health_data)
        self.db.commit()
        self.db.refresh(db_health_data)
        return db_health_data

