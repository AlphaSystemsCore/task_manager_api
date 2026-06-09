from fastapi import FastAPI, APIRouter, Depends
from app.auth.auth_dependency_jwt import get_current_user

router_tasks = APIRouter()

@router_tasks.post("/tasks")
async def create_task(user_id: str = Depends(get_current_user)):
    pass

@router_tasks.get("/tasks")
async def get_all_tasks(user_id: str = Depends(get_current_user)):
    pass

@router_tasks.put("/task/{task_id}")
async def update_task(user_id: str = Depends(get_current_user)):
    pass

@router_tasks.patch("/tasks/{task_id}")
async def update_task_partially(user_id: str = Depends(get_current_user)):
    pass

@router_tasks.get("/tasks/{task_id}")
async def get_task(user_id: str = Depends(get_current_user)):
    pass

