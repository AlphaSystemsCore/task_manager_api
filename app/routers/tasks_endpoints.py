from fastapi import FastAPI, APIRouter, Depends,Form, Query, HTTPException

from app.auth.auth_dependency_jwt import get_current_user
from app.schemas.task_schemas import TaskIN, Pagination
from app.services.task_service import create_task_service,get_all_tasks_service, get_task_by_name_service
router_tasks = APIRouter()

@router_tasks.post("/tasks")
async def create_task(task:TaskIN = Form(), user_id: str = Depends(get_current_user)):
    try:
        task_id = create_task_service(task.name, task.category, user_id, task.duration)
        return {"message":f"{task_id} -Task Created Successful"}
    except Exception as e:
        raise HTTPException(
            status_code = 400,
            detail=str(e)
        )

@router_tasks.get("/tasks")
async def get_all_tasks(user_id: str = Depends(get_current_user), pagination: Pagination = Query()):
    try:
        tasks = get_all_tasks_service(user_id, pagination.limit, pagination.offset)
        return tasks
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        
@router_tasks.get("/tasks/{name}")
def get_all_tasks_by_name(name:str, user_id: str = Depends(get_current_user)):
    task = get_task_by_name_service(user_id, name)
    return task

@router_tasks.put("/tasks/{task_id}")
async def update_task(user_id: str = Depends(get_current_user)):
    pass

@router_tasks.patch("/tasks/{task_id}")
async def update_task_partially(user_id: str = Depends(get_current_user)):
    pass

@router_tasks.get("/tasks/{task_id}")
async def get_task(user_id: str = Depends(get_current_user)):
    pass

