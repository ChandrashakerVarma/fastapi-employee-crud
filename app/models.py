from sqlalchemy import Column, Integer, String, Float, DateTime, func
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    position = Column(String(100), nullable=True)
    salary = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
