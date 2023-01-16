from fastapi import FastAPI
from os import getenv
from models.customers import *

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello world!"}
