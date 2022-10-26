from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from .cruds.internal.db_conection import SessionLocal
from sqlalchemy.orm import Session
from .cruds.schemas.departments import DepartmentSchema, Request, Response, RequestDepartment,DepartmentSchemaList
from .cruds import department  as crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_department_service(request: RequestDepartment, db: Session = Depends(get_db)):
    crud.create_department(db, department=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Department created successfully").dict(exclude_none=True)

@router.post("/create/multiple")
async def create_departments_service(requests: DepartmentSchemaList, db: Session = Depends(get_db)):
    for request in requests.parameter:
        crud.create_department(db, department=request)
    
    return Response(status="Ok",
                    code="200",
                    message="Departments created successfully").dict(exclude_none=True)


@router.get("/")
async def get_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _departments = crud.get_department(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_departments)

@router.get("/{department_id}")
async def get_department(department_id: int, db: Session = Depends(get_db)):
    _department = crud.get_department_by_id(db, department_id)
    
    return Response(status="Ok", code="200", message="Success fetch data", result=_department)


@router.patch("/update")
async def update_department(request: RequestDepartment, db: Session = Depends(get_db)):
    _department = crud.update_department(db, department_id=request.parameter.id,
                             department=request.parameter.department)
    return Response(status="Ok", code="200", message="Success update data", result=_department)


@router.delete("/delete")
async def delete_department(request: RequestDepartment,  db: Session = Depends(get_db)):
    crud.remove_department(db, department_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)



