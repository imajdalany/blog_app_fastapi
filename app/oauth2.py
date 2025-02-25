from fastapi import Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from app.router import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token_str: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = token.verify_token(
        token_str,
        credentials_exception,
    )

    return token_data
