from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.health_service import HealthService
from schemas.health_data import HealthDataCreate, HealthDataRead
from typing import List

health_router = APIRouter()

@health_router.post("/", response_model=HealthDataRead)
def create_health_data(health_data: HealthDataCreate, db: Session = Depends(get_db)):
    health_service = HealthService(db)
    return health_service.create_health_data(health_data)

@health_router.get("/{user_id}", response_model=List[HealthDataRead])
def get_health_data(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    health_service = HealthService(db)
    return health_service.get_health_data(user_id, skip, limit)
