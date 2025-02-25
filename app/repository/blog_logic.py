from fastapi import Depends, HTTPException, status
from app import models, schemas
from app.database import get_db
from sqlalchemy.orm import Session


def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


def get_blog_by_id(ID: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter_by(id=ID).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The requested id : {ID} is not available",
        )

    return blog


def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update_blog_by_id(ID: int, blog: schemas.Blog, db: Session = Depends(get_db)):
    blog_obj = db.query(models.Blog).filter_by(id=ID)

    if not blog_obj.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The requested id : {ID} is not available",
        )

    blog_obj.update(blog.model_dump())
    db.commit()

    return "updated successfully"


def delete_blog_by_id(ID: int, db: Session = Depends(get_db)):
    blog_obj = db.query(models.Blog).filter_by(id=ID)

    if not blog_obj.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The requested id : {ID} is not available",
        )

    blog_obj.delete(synchronize_session=False)
    db.commit()

    return f"Blog with id: {ID} is deleted successfully"
