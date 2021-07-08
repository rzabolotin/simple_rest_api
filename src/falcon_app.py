import falcon
from waitress import serve

from model import predict as model_predict


class PredictHandler:
    def on_post(self, req, resp):
        numbers = req.get_media()
        message = {"prediction": model_predict(numbers)}
        print(message)
        resp.media = message


app = falcon.App()
app.add_route('/predict', PredictHandler())


if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=5000)