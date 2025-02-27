from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.pydantic_settings import settings


engine = create_engine(settings.DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()
