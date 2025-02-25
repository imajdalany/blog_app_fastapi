from fastapi import FastAPI
from app.database import engine, Base
from app.router import blog, user, authorization

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(authorization.router)
app.include_router(blog.router)
app.include_router(user.router)
