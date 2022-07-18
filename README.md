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

docker run svc -d -p 8000:8000

```