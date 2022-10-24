from sqlalchemy.orm import Session
from .models import Department
from .schemas.departments import DepartmentSchema

def get_department(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Department).offset(skip).limit(limit).all()

def get_department_by_id(db: Session, department_id: int):
    return db.query(Department).filter(Department.id == department_id).first()

def create_department(db: Session, department: DepartmentSchema):
    _count = db.query(Department).count() +1
    _department = Department(id=_count, department=department.department)
    db.add(_department)
    db.commit()
    db.refresh(_department)
    return _department


def remove_department(db: Session, department_id: int):
    _department = get_department_by_id(db=db, department_id=department_id)
    db.delete(_department)
    db.commit()


def update_department(db: Session, department_id: int, department: str):
    _department = get_department_by_id(db=db, department_id=department_id)

    _department.department = department

    db.commit()
    db.refresh(_department)
    return _department
