from fastapi import FastAPI, APIRouter, Depends, Form, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from app.schemas.user_schema import UserCredentials
from app.services.auth_service import register_user_service  # fixed typo
from app.core.exeptions import EmailAlreadyExistsError


router_auth = APIRouter()

@router_auth.post("/auth/register")
async def register_user(user_credentials: UserCredentials):
    try:
        results = register_user_service(user_credentials.email, user_credentials.password)
        return results
    except EmailAlreadyExistsError as e:
        raise HTTPException(
            status_code=409,
            detail="Email already exists in the system"
        )
    

@router_auth.post("/auth/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    form_data.username
    form_data.password

@router_auth.get("/auth/logout/{uuid}")
async def logout_user(uuid: str):
    return {"user_id": uuid, "message": "Logged out"}
