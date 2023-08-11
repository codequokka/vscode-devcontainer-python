FROM python:3.8

WORKDIR /app

COPY ./requirements.txt /app
COPY ./requirements-dev.txt /app

RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
