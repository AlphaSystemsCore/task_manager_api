import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated 
from fastapi import HTTPException, status, Depends
from datetime import datetime, timezone, timedelta

from app.core.secrete_key_config import ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRES_MINUTES
from app.services.user_service import get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

async def get_current_user(token: str = Depends(oauth2_scheme)):
    #decoding and getting the payload
    CredentialError = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        # print(user_id)
        if user_id is None:
            raise CredentialError
        user = get_user(user_id)
        if user is None:
            raise CredentialError
        # print("Username:",user[0], "Role: ", user[1])
        return user_id
    except InvalidTokenError:
        raise CredentialError
   

def create_token(data: dict, expiry_delta: timedelta | None = None):
    #encoding the token
    to_encode = data.copy()
    if expiry_delta:
        exp = datetime.now(timezone.utc) + expiry_delta
    else:
        exp = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp":exp})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

    