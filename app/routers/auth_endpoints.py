from fastapi import FastAPI, APIRouter, Depends, Form, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from datetime import datetime, timezone, timedelta

from app.schemas.user_schema import UserCredentials
from app.services.auth_service import register_user_service, authenticate_user
from app.core.exeptions import EmailAlreadyExistsError, CredentialsError
from app.auth.auth_dependency_jwt import create_token


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
    try:
        user_id = authenticate_user(form_data.username, form_data.password)
        claim = {
            "sub":user_id
        }
        expiry_delta = timedelta(minutes=20)
        access_token = create_token(claim, expiry_delta)
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    except (CredentialsError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong username or password, please try again."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router_auth.get("/auth/logout/{uuid}")
async def logout_user(uuid: str):
    return {"user_id": uuid, "message": "Logged out"}
