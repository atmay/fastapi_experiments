from fastapi import FastAPI
from models import User, Poll

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/polls")
async def root():
    return {"polls": "Hello World"}


@app.post("/polls")
async def create_poll(poll: Poll):
    return poll


@app.get("/users")
async def root():
    return {"users": "Hello World"}


@app.post("/users")
async def create_user(user: User):
    return user
