import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated 
from fastapi import HTTPException, status
from datetime import datetime, timezone, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

async def get_current_user(token: str = Depends(oauth2_scheme)):
    CredentialError = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise CredentialError
        return user_id
    except InvalidTokenError:
        raise CredentialError
   

def create_token(data: dict, expiry_delta: timedelta | None = None):
    to_encode = data.copy()
    if expiry_delta:
        exp = datetime.now(timezone.utc) + expiry_delta
    else:
        exp = datetime.now(timezone.utc) + timedelta(minutes=30)

    to_encode.update({"exp":exp})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

    