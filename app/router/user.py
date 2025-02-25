from fastapi import Depends, status, HTTPException, APIRouter
from app import models, schemas
from app.database import get_db
from sqlalchemy.orm import Session
from app.repository import user_logic

router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowUser,
)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return user_logic.create_user(user, db)


@router.get(
    "/{ID}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowUser,
)
def get_user_by_id(ID: int, db: Session = Depends(get_db)):
    return user_logic.get_user_by_id(ID, db)
