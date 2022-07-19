# svc-humor

## Build and start the app locally
```
poetry shell

poetry install

poetry run uvicorn svc:app --reload

```

## Build and start the app in production
```
docker build -t svc .

docker run -d -p 80:80 svc

```