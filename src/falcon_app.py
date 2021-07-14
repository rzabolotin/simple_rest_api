import falcon
from waitress import serve
from loguru import logger

from model import predict as model_predict


class PredictHandler:
    def on_post(self, req, resp):
        numbers = req.get_media()
        logger.info(f"Got request for prediction {numbers}")
        prediction = model_predict(numbers)
        logger.success(f"Calculated the prediction = {prediction}")
        resp.media = {"prediction": prediction}


app = falcon.App()
app.add_route('/predict', PredictHandler())


if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=5000)