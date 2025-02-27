from fastapi import Depends, HTTPException, status
from app import models, schemas
from app.database import get_db
from sqlalchemy.orm import Session
from typing import Annotated

database_dependency = Annotated[Session, Depends(get_db)]


def get_all_blogs(db: database_dependency):
    blogs = db.query(models.Blog).all()
    return blogs


def get_blog_by_id(ID: int, db: database_dependency):
    blog = db.query(models.Blog).filter_by(id=ID).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The requested id : {ID} is not available",
        )

    return blog


def create_blog(
    blog: schemas.Blog,
    current_username: str,
    db: database_dependency,
):
    current_id = db.query(models.User).filter_by(username=current_username).first().id

    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=current_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update_blog_by_id(ID: int, blog: schemas.Blog, db: database_dependency):
    blog_obj = db.query(models.Blog).filter_by(id=ID)

    if not blog_obj.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The requested id : {ID} is not available",
        )

    blog_obj.update(blog.model_dump())
    db.commit()

    return "updated successfully"


def delete_blog_by_id(ID: int, db: database_dependency):
    blog_obj = db.query(models.Blog).filter_by(id=ID)

    if not blog_obj.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The requested id : {ID} is not available",
        )

    blog_obj.delete(synchronize_session=False)
    db.commit()

    return f"Blog with id: {ID} is deleted successfully"
