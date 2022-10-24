from fastapi import FastAPI, Request
from routers.cruds import models
from routers import departments, jobs, hired_employees
from routers.cruds.internal.db_conection import engine

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")
app = FastAPI()

# apis
app.include_router(jobs.router, prefix="/job", tags=["job"])
app.include_router(departments.router, prefix="/department", tags=["department"])
app.include_router(hired_employees.router, prefix="/employee", tags=["employee"])

# views
@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

@app.get("/report1")
async def root(request:Request):
    
    with engine.connect() as conn:
        df = pd.read_sql_table(table_name='report1',con=conn)
        
    return templates.TemplateResponse(
        'df_representation.html',
        {'request': request, 'data': df.to_html()}
    )
    