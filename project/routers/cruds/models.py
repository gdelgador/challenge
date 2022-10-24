from typing import List
from sqlalchemy import  Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
from .internal.db_conection import Base

class Department(Base):
    __tablename__ ="departments"
    
    id = Column(Integer, primary_key=True, index=True)
    department= Column(String)
    
class Job(Base):
    __tablename__ ="jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    job= Column(String)
    
class HiredEmployee(Base):
    __tablename__ ="hired_employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String)
    datetime= Column(String)
    department_id= Column(Integer, ForeignKey("departments.id"))
    job_id= Column(Integer, ForeignKey("jobs.id"))
    
    # job = relationship("Department", back_populates="owner")
    # job = relationship("Job", back_populates="owner")
    
