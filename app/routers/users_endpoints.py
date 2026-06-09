from fastapi import FastAPI, APIRouter

router_users = APIRouter()
@router_users.get("/users/profile")
async def get_user_profile():
    pass

@router_users.put("/users/")
async def update_profile():
    pass

@router_users.patch("/users/")
async def update_profile_partially():
    pass