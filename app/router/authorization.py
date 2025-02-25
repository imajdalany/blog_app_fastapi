from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models
from sqlalchemy.orm import Session
from app.database import get_db
from app import hashing
from . import token
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from app.logging import timed

router = APIRouter(tags=["Authorization"])


@router.post("/login")
@timed
def login(login: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(username=login.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The requested username or password is not correct",
        )

    if not hashing.Hash.verify(user.password, login.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The requested username or password is not correct",
        )

    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")
