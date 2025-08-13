from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

def create_employee(db: Session, employee: schemas.EmployeeCreate) -> models.Employee:
    db_emp = models.Employee(**employee.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def get_employee(db: Session, employee_id: int) -> Optional[models.Employee]:
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 100) -> List[models.Employee]:
    return db.query(models.Employee).offset(skip).limit(limit).all()

def update_employee(db: Session, employee_id: int, emp_update: schemas.EmployeeUpdate) -> Optional[models.Employee]:
    db_emp = get_employee(db, employee_id)
    if not db_emp:
        return None
    update_data = emp_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_emp, key, value)
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def delete_employee(db: Session, employee_id: int) -> Optional[models.Employee]:
    db_emp = get_employee(db, employee_id)
    if not db_emp:
        return None
    db.delete(db_emp)
    db.commit()
    return db_emp
