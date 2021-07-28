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


@app.route('/form_predict', methods=['POST'])
def form_predict():
    numbers = [
        request.form["num1"],
        request.form["num2"],
        request.form["num3"],
        request.form["num4"],
    ]
    logger.info(f"Got request for prediction {numbers}")
    prediction = model_predict(numbers)
    logger.success(f"Calculated the prediction = {prediction}")
    return f"""
    Your model prediction is <b>{prediction}</b>
    """


@app.route('/form')
def form():
    return """
    <html>
        <body>
        <form method="POST" action="form_predict" >
            <input type="number" step="0.01" name="num1" min="0" max="100"><br>
            <input type="number" step="0.01" name="num2" min="0" max="100"><br>
            <input type="number" step="0.01" name="num3" min="0" max="100"><br>
            <input type="number" step="0.01" name="num4" min="0" max="100"><br>
            <button type="submit">Отправить</button><br>
        </form>
    
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run()
