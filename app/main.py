from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, get_db


app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}


app = FastAPI(title="Employees API")


@app.post("/employees/", response_model=schemas.EmployeeRead, status_code=status.HTTP_201_CREATED)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
   
    existing = db.query(models.Employee).filter(models.Employee.email == employee.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_employee(db, employee)

@app.get("/employees/", response_model=list[schemas.EmployeeRead])
def list_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_employees(db, skip=skip, limit=limit)

@app.get("/employees/{employee_id}", response_model=schemas.EmployeeRead)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_emp = crud.get_employee(db, employee_id)
    if not db_emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_emp

@app.put("/employees/{employee_id}", response_model=schemas.EmployeeRead)
def update_employee(employee_id: int, emp_update: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    updated = crud.update_employee(db, employee_id, emp_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated

@app.delete("/employees/{employee_id}", response_model=schemas.EmployeeRead)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_employee(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return deleted
