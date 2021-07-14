from flask import Flask, request, jsonify
from loguru import logger

from model import predict as model_predict

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def predict():
    numbers = request.json
    logger.info(f"Got request for prediction {numbers}")
    prediction = model_predict(numbers)
    logger.success(f"Calculated the prediction = {prediction}")
    return jsonify({"prediction": prediction})


if __name__ == '__main__':
    app.run()
