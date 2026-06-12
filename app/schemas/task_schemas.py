from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime
from typing import Optional

class TaskIN(BaseModel):
    name: str 
    category: Literal["personal", "school", "leisure", "job"]
    duration: str
    
class Pagination(BaseModel):
    limit: int = Field(10, ge=1, le=25)
    offset: int = Field(0, ge=0)

class TasksOut(BaseModel):
    task_id:str
    name: str
    category: str
    status: str
    time_created: datetime
    duration: str
    time_completed: datetime | None = None

class To_Be_Updated(BaseModel):
    name:str|None = None
    category:Optional[Literal["personal", "school", "leisure", "job",""]] = None
    time_to_be_completed:str | None = None

class Update_Status(BaseModel):
    task_id:str
    status:Optional[Literal['pending', 'completed', 'canceled']] = None
