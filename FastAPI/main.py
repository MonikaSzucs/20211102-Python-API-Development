from types import BuiltinMethodType
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    # performs validation and returns error if both title and content are not provided
    title: str
    content: str
    # optional for user to add info
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "Welcome to my API check out the about section "}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    # Convert posts to dictionary using .dic
    print(post.dict())
    print(post.rating)
    return {"data": post}
    # title str, content str, category, Bool published
