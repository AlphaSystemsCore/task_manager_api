from fastapi import FastAPI, APIRouter

router_tasks = APIRouter()

@router_tasks.post("/tasks")
async def create_task():
    pass

@router_tasks.get("/tasks")
async def get_all_tasks():
    pass

@router_tasks.put("/task/{task_id}")
async def update_task():
    pass

@router_tasks.patch("/tasks/{task_id}")
async def update_task_partially():
    pass

@router_tasks.get("/tasks/{task_id}")
async def get_task():
    pass

