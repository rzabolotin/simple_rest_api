from typing import List

from fastapi import FastAPI

from model import predict as model_predict

app = FastAPI()


@app.post("/predict")
async def predict(numbers: List[float]):
    message = {"prediction": model_predict(numbers)}
    print(message)
    return message

