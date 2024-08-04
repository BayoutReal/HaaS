# tests/test_health.py
import pytest
from fastapi.testclient import TestClient
from api.main import app
from db.session import get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.health_data import HealthData

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

def test_create_health_data():
    response = client.post(
        "/health/",
        json={"user_id": 1, "steps": 10000, "heart_rate": 60.0, "calories_burned": 500.0, "sleep_hours": 7.0, "timestamp": "2023-01-01T00:00:00"}
    )
    assert response.status_code == 200
    assert response.json()["steps"] == 10000

def test_get_health_data():
    response = client.get("/health/1")
    assert response.status_code == 200
    assert len(response.json()) > 0
