from fastapi import FastAPI, APIRouter, Depends
from app.auth.auth_dependency_jwt import get_current_user

router_users = APIRouter()
@router_users.get("/users/profile")
async def get_user_profile(user_id: str  = Depends(get_current_user)):
    pass

@router_users.put("/users/")
async def update_profile(user_id: str  = Depends(get_current_user)):
    pass

@router_users.patch("/users/")
async def update_profile_partially(user_id: str  = Depends(get_current_user)):
    pass