# db/init_db.py
from sqlalchemy.orm import Session
from db.base_class import Base
from db.session import engine
from models import user, health_data

def init_db():
    Base.metadata.create_all(bind=engine)