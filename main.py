from model import model_pipeline
from typing import Union
from fastapi import FastAPI, UploadFile
import io
from PIL import Image

app = FastAPI()

@app.get("/")
def read_get():
    return {"message": "HELLO WORLD"}



@app.post("/ask")
def ask(text: str, image: UploadFile):
    # read file from the uploadfile image
    content = image.file.read()

    image = Image.open(io.BytesIO(content))
    # image = Image(image.file)

    result = model_pipeline(text, image)

    return {"result": result}
