import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_user_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/", json={"email": "testuser@example.com", "password": "testpass"})
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"
