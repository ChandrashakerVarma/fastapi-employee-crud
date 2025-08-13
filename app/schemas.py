from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    position: Optional[str] = None
    salary: Optional[float] = None

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None

class EmployeeRead(EmployeeBase):
    id: int
    created_at: datetime

    class Config:
       from_attribute= True
