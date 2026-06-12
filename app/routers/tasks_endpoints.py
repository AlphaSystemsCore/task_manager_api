from fastapi import (
 FastAPI,
 APIRouter, 
 Depends,
 Form, 
 Query,
 status,
 HTTPException)
from typing import Annotated
from uuid import UUID

from app.auth.auth_dependency_jwt import get_current_user
from app.schemas.task_schemas import TaskIN, Pagination,Update_Status, TasksOut, To_Be_Updated
from app.services.task_service import (
    create_task_service,
    get_tasks_service,
    get_task_by_name_service,
    update_task_service, 
    update_status_service,
    delete_task_service
    )

router_tasks = APIRouter()

@router_tasks.post("/tasks")
async def create_task(
    user_id: Annotated[str, Depends(get_current_user)], 
    task:TaskIN = Form()
    ):
    try:
        task_id = create_task_service(task.name, task.category, user_id, task.duration)
        
    except Exception as e:
        raise HTTPException(
            status_code = 400,
            detail=str(e)
        )
    else:
        if task_id:
            return {"message": f"Task id: {task_id[0]}, Created successfully."}


@router_tasks.get("/tasks/", response_model=list[TasksOut])
def get_tasks(user_id: Annotated[str, Depends(get_current_user)], pagination:Pagination = Query()):
    #endpoints to return tasks
    try:
        tasks = get_tasks_service(user_id, pagination.limit, pagination.offset)
    except Exception as e:
        # log
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    else:
        return tasks

@router_tasks.get("/tasks/{task_name}", response_model=TasksOut)
def get_task_by_name(task_name:str, user_id: Annotated[UUID, Depends(get_current_user)]):
    # read a task by name
    try:
        task = get_task_by_name_service(user_id, task_name)
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    else:
        return task

@router_tasks.put("/tasks/{task_id}")
def update_task(task_id:UUID, user_id: UUID = Depends(get_current_user), field:To_Be_Updated = Form()):
    try:
        if not field.category:
            field.category = None
        update_task_service(user_id, str(task_id), field.name, field.category, field.time_to_be_completed)
        return {"message":"Update successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router_tasks.patch("/tasks/status/")
def update_status(
    field: Update_Status,
    user_id: str = Depends(get_current_user)
):
    try:
        return update_status_service(user_id, field.new_status, field.task_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router_tasks.delete("/tasks/{task_id}")
def delete_task(task_id:str, user_id: Annotated[str, Depends(get_current_user)]):
    try:
        return delete_task_service(user_id, task_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
        # 4c24455e-d6e1-40dc-a3cf-ba7754428a93