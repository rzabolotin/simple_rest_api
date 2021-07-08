import requests


def send_test():
    r = requests.post("http://localhost:5000/predict", json=[1, 2, 3, 4.44])
    r.raise_for_status()
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    send_test()
