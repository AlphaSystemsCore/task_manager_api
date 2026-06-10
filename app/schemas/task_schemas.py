from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

class TaskIN(BaseModel):
    name: str 
    category: Literal["personal", "school", "leisure", "job"]
    duration: str
    
class Pagination(BaseModel):
    limit: int = Field(10, ge=1, le=25)
    offset: int = Field(0, ge=0)

class TasksOut(BaseModel):
    name: str
    category: str
    status: str
    time_created: datetime
    duration: str
    time_completed: datetime | None = None
