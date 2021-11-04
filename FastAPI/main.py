from types import BuiltinMethodType
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
def root():
    return {"message": "Welcome to my API check out the about section "}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    # print(post)
    # Convert posts to dictionary using .dic
    # print(post.dict())
    my_posts.append(post_dict)
    return {"data": post_dict}
    # title str, content str, category, Bool published


# path parameter using the ID
@app.get("/posts/{id}")
# def get_post(id: int, response: Response):
def get_post(id: int):
    print(type(id))
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    return {"post_detail": post}
    # return {"post_detail": f"Here is post {id}"}


@app.delete("/posts/{id}")
def delete_post(id):
    # deleting posts
    # find the index in the array that has reuqired ID
    # my_posts.pop(index)
    index = find_index_post(id)
    my_posts.pop(index)
    return {'message': 'post was successfully deleted'}
