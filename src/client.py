import requests
from loguru import logger

def send_test():
    logger.debug("Sending post request to local server")
    r = requests.post("http://localhost:5000/predict", json=[1, 2, 3, 4.44])
    r.raise_for_status()
    logger.debug(f"Got response status code: {r.status_code}")
    logger.info(f"Got answer from server: {r.text}")


if __name__ == '__main__':
    send_test()
