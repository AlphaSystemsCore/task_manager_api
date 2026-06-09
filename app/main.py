from fastapi import FastAPI
from app.routers.auth_endpoints import router_auth
from app.routers.tasks_endpoints import router_tasks
from app.routers.users_endpoints import router_users

app = FastAPI()
app.include_router(router_auth)
app.include_router(router_tasks)
app.include_router(router_users)