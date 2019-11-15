FROM python:3.7-alpine
ENV PYTHONBUFFERED 1
RUN apk add --no-cache bash

RUN mkdir /mysite
RUN mkdir /db
COPY ./requirements.txt /mysite/
COPY ./manage.py /mysite/
RUN pip install -r /mysite/requirements.txt

RUN mkdir -p /mysite/mysite
WORKDIR /mysite
COPY ./mysite /mysite/mysite

RUN adduser -D ubuntu
USER ubuntu
