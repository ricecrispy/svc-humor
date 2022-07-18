# download python 3.10 image
FROM python:3.10-bullseye
RUN apt-get update
RUN apt-get install curl -y

WORKDIR /app

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
COPY svc.py svc.py

# Install poetry
RUN pip install "poetry==1.1.14"

# install project packages
RUN poetry install --no-dev

# start app
CMD poetry run gunicorn -w 4 -k uvicorn.workers.UvicornWorker svc:app