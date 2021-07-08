from flask import Flask, request, jsonify

from model import predict as model_predict

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def predict():
    numbers = request.json
    message = {"prediction": model_predict(numbers)}
    print(message)
    return jsonify(message)


if __name__ == '__main__':
    app.run()
