from types import BuiltinMethodType
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    # performs validation and returns error if both title and content are not provided
    title: str
    content: str


@app.get("/")
def root():
    return {"message": "Welcome to my API check out the about section "}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.title)
    return {"data": "new post"}
    # title str, content str, category, Bool published
