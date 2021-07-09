# simple_rest_api
In this repo I created a several APIs using:
- Flask
- FastAPI
- Falcon

And also I created two Dockerfiles to deploy flask service
- with uwsgi
- with nginx+uwsgi

# how to run

## flask
```shell
python src\flask_app.py
```

## falcon
```shell
python src\falllcon_app.py
```

## fast_api
```shell
cd src
uvicorn fast_api_app:app --port 5000 --reload
```

## client (to test that service is working)
```shell
python src\client.py
```

# Docker

To run service in docker-compose with uwsgi
```shell
mv Dockerfile.uwsgi Dockerfile
docker-compose -f docker-compose-check.yml up -d
```

To run service in docker-compose with nginx+uwsgi
```shell
mv Dockerfile.nginx Dockerfile
docker-compose -f docker-compose-check.yml up -d
```