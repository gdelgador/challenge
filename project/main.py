from fastapi import FastAPI
from routers.cruds import models
from routers import departments, jobs, hired_employees
from routers.cruds.internal.db_conection import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(jobs.router, prefix="/job", tags=["job"])
app.include_router(departments.router, prefix="/department", tags=["department"])
app.include_router(hired_employees.router, prefix="/employee", tags=["employee"])

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}