from sqlalchemy.orm import Session
from fastapi import HTTPException
from .models import Department
from .schemas.departments import DepartmentSchema

def get_department(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Department).offset(skip).limit(limit).all()

def get_department_by_id(db: Session, department_id: int):
    _department = db.query(Department).filter(Department.id == department_id).first() 
    
    if not _department:
        raise HTTPException(status_code=400, detail="DepartmentID not found.")
    return _department

def create_department(db: Session, department: DepartmentSchema):
    _department = Department(id=department.id, department=department.department)
    
    try:
        db.add(_department)
        db.commit()
        db.refresh(_department)
        return _department
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unexpected error happends, {e}")


def remove_department(db: Session, department_id: int):
    _department = get_department_by_id(db=db, department_id=department_id)
    db.delete(_department)
    db.commit()


def update_department(db: Session, department_id: int, department: str):
    _department = get_department_by_id(db=db, department_id=department_id)
    
    try:
        _department.department = department
        db.commit()
        db.refresh(_department)
        return _department
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unexpected error happends, {e}")