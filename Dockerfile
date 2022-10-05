FROM python:3.7-slim

ENV PORT  80
ENV PYTHONUNBUFFERED 1

EXPOSE $PORT

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  build-essential \
  gcc python3-dev

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . /code
WORKDIR /code

