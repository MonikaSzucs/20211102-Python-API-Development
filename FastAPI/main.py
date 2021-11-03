from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to my API check out the about section "}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}
