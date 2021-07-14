from typing import List
from fastapi import FastAPI
from loguru import logger
from model import predict as model_predict


app = FastAPI()


@app.post("/predict")
async def predict(numbers: List[float]):
    logger.info(f"Got request for prediction {numbers}")
    prediction = model_predict(numbers)
    logger.success(f"Calculated the prediction = {prediction}")
    return {"prediction": prediction}


