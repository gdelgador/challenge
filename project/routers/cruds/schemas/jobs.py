from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')
        
class JobSchema(BaseModel):
    id: Optional[int] = None
    job: Optional[str]=None
    
    class Config:
        orm_mode=True
        
class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)
    
class JobSchemaList(BaseModel):
    parameter: List[JobSchema]

class RequestJob(BaseModel):
    parameter: JobSchema = Field(...)
    
class RequestJobList(BaseModel):
    parameter: JobSchemaList = Field(...)
    
class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]