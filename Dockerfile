FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2
RUN pip install -r requirements.txt \

