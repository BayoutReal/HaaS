from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base_class import Base
from models.user import User

def setup_function():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)  # Create tables
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_user_model():
    SessionLocal = setup_function()
    db = SessionLocal()
    test_user = User(email="user@example.com", hashed_password="hashedpassword")
    db.add(test_user)
    db.commit()
    user = db.query(User).first()
    assert user.email == "user@example.com"
    db.close()
