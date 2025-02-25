from fastapi import Depends, status, APIRouter
from app import schemas
from app.database import get_db
from sqlalchemy.orm import Session
from app.repository import user_logic
from app.logging import timed

router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowUser,
)
@timed
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return user_logic.create_user(user, db)


@router.get(
    "/{ID}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowUser,
)
@timed
def get_user_by_id(ID: int, db: Session = Depends(get_db)):
    return user_logic.get_user_by_id(ID, db)
