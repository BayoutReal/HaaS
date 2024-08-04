from pydantic import BaseModel, EmailStr
from typing import List

from schemas.health_data import HealthDataRead


class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class UserWithHealthData(UserRead):
    health_data: List[HealthDataRead] = []
