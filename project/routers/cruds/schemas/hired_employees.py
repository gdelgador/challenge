from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class HiredEmployeeSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str]=None
    datetime: Optional[str]=None
    department_id: Optional[int]=None
    job_id: Optional[int]=None
    
    class Config:
        orm_mode=True
    
class HiredEmployeeSchemaList(BaseModel):
    parameter: List[HiredEmployeeSchema]
    
class RequestHiredEmployeeSchemaList(BaseModel):
    parameter: HiredEmployeeSchemaList = Field(...)
    
class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestHiredEmployee(BaseModel):
    parameter: HiredEmployeeSchema = Field(...)
    
class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]