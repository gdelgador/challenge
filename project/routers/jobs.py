from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from .cruds.internal.db_conection import SessionLocal
from sqlalchemy.orm import Session
from .cruds.schemas.jobs import JobSchema, Request, Response, RequestJob
from .cruds import job as crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# JOBS
@router.post("/create")
async def create_job_service(request: RequestJob, db: Session = Depends(get_db)):
    crud.create_job(db, job=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Job created successfully").dict(exclude_none=True)

@router.get("/")
async def get_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _jobs = crud.get_job(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_jobs)


@router.get("/{job_id}")
async def get_employee(job_id: int, db: Session = Depends(get_db)):
    _job = crud.get_job_by_id(db, job_id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_job)


@router.patch("/update")
async def update_job(request: RequestJob, db: Session = Depends(get_db)):
    _job = crud.update_job(db, job_id=request.parameter.id,
                             job=request.parameter.job)
    return Response(status="Ok", code="200", message="Success update data", result=_job)


@router.delete("/delete")
async def delete_job(request: RequestJob,  db: Session = Depends(get_db)):
    crud.remove_job(db, job_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)