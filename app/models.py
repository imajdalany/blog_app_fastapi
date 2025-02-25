from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blog_table"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(50))
    body = Column(String)
    user_id = Column(Integer, ForeignKey("user_table.id"))

    user = relationship("User", back_populates="blog")

class User(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)

    name= Column(String(50))
    username= Column(String(50))
    password= Column(String(50))

    blog = relationship("Blog", back_populates="user")