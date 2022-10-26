from sqlalchemy.orm import Session
from .models import Job
from .schemas.jobs import JobSchema


def get_job(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Job).offset(skip).limit(limit).all()

def get_job_by_id(db: Session, job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()

def create_job(db: Session, job: JobSchema):
    _job = Job(id=job.id,job=job.job)
    db.add(_job)
    db.commit()
    db.refresh(_job)
    return _job

def remove_job(db: Session, job_id: int):
    _job = get_job_by_id(db=db, job_id=job_id)
    db.delete(_job)
    db.commit()

def update_job(db: Session, job_id: int, job: str):
    _job = get_job_by_id(db=db, job_id=job_id)

    _job.job = job

    db.commit()
    db.refresh(_job)
    return _job