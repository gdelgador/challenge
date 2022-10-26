from unicodedata import name
from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import HiredEmployee
from .schemas.hired_employees import HiredEmployeeSchema
from datetime import datetime

def get_employee(db: Session, skip: int = 0, limit: int = 100):
    return db.query(HiredEmployee).offset(skip).limit(limit).all()

def get_employee_by_id(db: Session, hired_employee_id: int):
    _employee = db.query(HiredEmployee).filter(HiredEmployee.id == hired_employee_id).first()

    if not _employee:
        raise HTTPException(status_code=400, detail="EmployeeID not found.")
    return _employee

def create_employee(db: Session, hired_employee: HiredEmployeeSchema):
    _hired_employee = HiredEmployee(id=hired_employee.id,
                                    name=hired_employee.name,
                                    datetime = (datetime.now()).isoformat(), 
                                    department_id = hired_employee.department_id,
                                    job_id = hired_employee.job_id
                                    )
    try:    
        db.add(_hired_employee)
        db.commit()
        db.refresh(_hired_employee)
        return _hired_employee
    except Exception as e:
         raise HTTPException(status_code=400, detail=f"Unexpected error happends, {e}")


def remove_employee(db: Session, hired_employee_id: int):
    _hired_employee = get_employee_by_id(db=db, hired_employee_id=hired_employee_id)
    db.delete(_hired_employee)
    db.commit()


def update_employee(db: Session, hired_employee_id: int, name: str, department_id:int, job_id:int):
    _hired_employee = get_employee_by_id(db=db, hired_employee_id=hired_employee_id)
    
    try:
        
        _hired_employee.name = name
        _hired_employee.department_id = department_id
        _hired_employee.job_id = job_id

        db.commit()
        db.refresh(_hired_employee)
        return _hired_employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unexpected error happends, {e}")
