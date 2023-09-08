from model import model_pipeline
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_get():
    return {"message": "hELLO WORLD"}

