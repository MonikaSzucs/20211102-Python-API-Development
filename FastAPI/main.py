from types import BuiltinMethodType
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    # performs validation and returns error if both title and content are not provided
    title: str
    content: str
    # optional for user to add info
    published: bool = True
    rating: Optional[int] = None

# This is just stored in memory. This gets updated each time you restart the program.
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favourite foots", "content": "I like pizza", "id": 2}
            ]


@app.get("/")
def root():
    return {"message": "Welcome to my API check out the about section "}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    #print(post)
    # Convert posts to dictionary using .dic
    # print(post.dict())
    my_posts.append(post_dict)
    return {"data": post_dict}
    # title str, content str, category, Bool published


# path parameter using the ID
@app.get("/posts/{id}")
def get_post(id):
    print(id)
    return {"post_detail": f"Here is post {id}"}