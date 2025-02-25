from fastapi import Depends, status, HTTPException, APIRouter
from app import models, schemas
from app.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.repository import blog_logic
from app.oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowBlog,
)
def create_blog(
    blog: schemas.Blog,
    db: Session = Depends(get_db),
    get_current_user: schemas.User = Depends(get_current_user),
):
    return blog_logic.create_blog(blog, db)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.ShowBlog],
)
def get_all_blogs(
    db: Session = Depends(get_db),
    get_current_user: schemas.User = Depends(get_current_user),
):
    return blog_logic.get_all_blogs(db)


@router.get(
    "/{ID}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog,
)
def get_blog_by_id(
    ID: int,
    db: Session = Depends(get_db),
    get_current_user: schemas.User = Depends(get_current_user),
):
    return blog_logic.get_blog_by_id(ID, db)


@router.delete("/{ID}", status_code=status.HTTP_200_OK)
def delete_blog_by_id(
    ID: int,
    db: Session = Depends(get_db),
    get_current_user: schemas.User = Depends(get_current_user),
):
    return blog_logic.delete_blog_by_id(ID, db)


@router.put("/{ID}", status_code=status.HTTP_202_ACCEPTED)
def update_blog_by_id(
    ID: int,
    blog: schemas.Blog,
    db: Session = Depends(get_db),
    get_current_user: schemas.User = Depends(get_current_user),
):
    return blog_logic.update_blog_by_id(ID, blog, db)
