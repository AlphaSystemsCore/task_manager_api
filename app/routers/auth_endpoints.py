from fastapi import FastAPI, APIRouter, Depends, Form, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from app.schemas.user_schema import UserCredentials
from app.services.auth_service import register_user_service  # fixed typo

router_auth = APIRouter()

@router_auth.post("/auth/register")
async def register_user(user_credentials: UserCredentials):
    try:
        results = register_user_service(user_credentials.email, user_credentials.password)
        if results is None:
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists in the system"
        )
        return results
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    

@router_auth.post("/auth/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    # call your login service here
    return {"email":form_data.username, "message": "Login successful"}

@router_auth.get("/auth/logout/{uuid}")
async def logout_user(uuid: str):
    return {"user_id": uuid, "message": "Logged out"}
