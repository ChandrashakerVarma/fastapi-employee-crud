import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv() 

DATABASE_URL = os.getenv("DATABASE_URL")

# create sync engine for SQLAlchemy (not async)
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

# session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative base
Base = declarative_base()

# dependency for FastAPI endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
