from fastapi import (
 FastAPI,
 APIRouter, 
 Depends,
 Form, 
 Query,
 status,
 HTTPException)
from typing import Annotated

from app.auth.auth_dependency_jwt import get_current_user
from app.schemas.task_schemas import TaskIN, Pagination, TasksOut
from app.services.task_service import (
    create_task_service,
    get_tasks_service
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
        return {"message": f"Task id: {task_id}, Created successfully."}


@router_tasks.get("/tasks/", response_model=list[TasksOut])
def get_tasks(user_id: Annotated[str, Depends(get_current_user)], pagination:Pagination = Query()):
    tasks = get_tasks_service(user_id, pagination.limit, pagination.offset)
    try:
        if tasks is not None:
            return [
                TasksOut(
                name=task[0],
                category=task[1],
                status=task[2],
                time_created=task[3],
                duration=task[4],
                time_completed=task[5]
            )
            for task in tasks]
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No task found"
            )
    except Exception as e:
        # log
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No task found"
        )

