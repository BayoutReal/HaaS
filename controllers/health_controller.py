from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.health_service import HealthService
from schemas.health_data import HealthDataCreate, HealthDataRead

health_router = APIRouter()

@health_router.post("/", response_model=HealthDataRead)
def create_health_data(health_data: HealthDataCreate, db: Session = Depends(get_db)):
    health_service = HealthService(db)
    return health_service.create_health_data(health_data)

