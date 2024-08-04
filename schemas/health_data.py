from pydantic import BaseModel

class HealthDataCreate(BaseModel):
    user_id: int
    steps: int
    sleep_hours: float

class HealthDataRead(BaseModel):
    id: int
    user_id: int
    steps: int
    sleep_hours: float

    class Config:
        orm_mode = True
