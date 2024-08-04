from services.user_service import UserService
from models.user import User
from schemas.user import UserCreate

def test_create_user(db_session):
    user_data = UserCreate(email="test@example.com", password="strongpassword")
    user_service = UserService(db=db_session)
    new_user = user_service.create_user(user_data)
    assert new_user.email == "test@example.com"
