FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV LISTEN_PORT 5000
RUN pip install uwsgi flask sklearn numpy

WORKDIR /app
COPY src /app
COPY models /app/models

RUN mv /app/flask_app.py /app/main.py