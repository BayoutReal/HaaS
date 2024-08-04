from httpx import AsyncClient
import pytest
from main import app  # Ensure this import reflects the path to your FastAPI app

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/", json={"email": "test@example.com", "password": "strongpassword"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
