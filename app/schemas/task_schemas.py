from pydantic import BaseModel
from typing import Literal

class TaskIN(BaseModel):
    name: str 
    category: Literal["personal", "school", "leisure", "job"]
    duration: str
    
class Pagination(BaseModel):
    limit: int = 10
    offset: int = 0