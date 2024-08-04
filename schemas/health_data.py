# schemas/health_data.py
from pydantic import BaseModel
from datetime import datetime

class HealthDataCreate(BaseModel):
    user_id: int
    steps: int
    heart_rate: float
    calories_burned: float
    sleep_hours: float
    timestamp: datetime

class HealthDataRead(HealthDataCreate):
    id: int

    class Config:
        orm_mode = True
