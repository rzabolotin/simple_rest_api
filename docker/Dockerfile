FROM python:3.9

RUN apt-get update -y && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN pip install --upgrade pip
RUN pip install uwsgi flask sklearn numpy

WORKDIR /app
COPY ../src /app
COPY ../models /app/models

CMD ["uwsgi", "--http", ":5000", "--module", "flask_app:app", "--processes", "4", "--master"]