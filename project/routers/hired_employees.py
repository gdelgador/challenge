from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from .cruds.internal.db_conection import SessionLocal
from sqlalchemy.orm import Session
from .cruds.schemas.hired_employees import HiredEmployeeSchema, Request, Response, RequestHiredEmployee, HiredEmployeeSchemaList
from .cruds import hired_employees as crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create_employee_service(request: RequestHiredEmployee, db: Session = Depends(get_db)):
    crud.create_employee(db, hired_employee=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Job created successfully").dict(exclude_none=True)

@router.post("/create/multiple")
async def create_employees_service(requests: HiredEmployeeSchemaList, db: Session = Depends(get_db)):
    for request in requests.parameter:
        crud.create_department(db, department=request)
    
    return Response(status="Ok",
                    code="200",
                    message="Employees created successfully").dict(exclude_none=True)


@router.get("/")
async def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _hired_employees = crud.get_employee(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_hired_employees)

@router.get("/{hired_employee_id}")
async def get_employee(hired_employee_id: int, db: Session = Depends(get_db)):
    _hired_employee = crud.get_employee_by_id(db, hired_employee_id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_hired_employee)


@router.patch("/update")
async def update_employee(request: RequestHiredEmployee, db: Session = Depends(get_db)):
    _hired_employees = crud.update_employee(db,
                                            hired_employee_id=request.parameter.id,
                                            name=request.parameter.name,
                                            department_id=request.parameter.department_id,
                                            job_id=request.parameter.job_id
                                            )
    return Response(status="Ok", code="200", message="Success update data", result=_hired_employees)


@router.delete("/delete")
async def delete_employee(request: RequestHiredEmployee,  db: Session = Depends(get_db)):
    crud.remove_employee(db, hired_employee_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)