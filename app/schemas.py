from pydantic import BaseModel
from typing import List


class Blog(BaseModel):
    title: str
    body: str


class Blog_Base(Blog):
    class Config:
        from_attributes = True


class User(BaseModel):
    name: str
    username: str
    password: str


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class ShowUser(BaseModel):
    name: str
    username: str
    blog: List[Blog] = []

    class Config:
        from_attributes = True


class ShowBlog(BaseModel):
    title: str
    body: str
    user: ShowUser

    class Config:
        from_attributes = True
