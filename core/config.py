class Settings:
    DATABASE_URL = "sqlite:///./app.db"
    SECRET_KEY = "your_secret_key_here"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()
