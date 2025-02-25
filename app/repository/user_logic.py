from fastapi import Depends, status, HTTPException
from app import models, schemas
from app.database import get_db
from sqlalchemy.orm import Session
from app.hashing import Hash


def create_user(user: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=user.name, username=user.username, password=Hash.encrypt(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_id(ID: int, db: Session = Depends(get_db)):
    user_obj = db.query(models.User).filter_by(id=ID)

    if not user_obj.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The requested id : {ID} is not available",
        )

    user = user_obj.first()
    return user
