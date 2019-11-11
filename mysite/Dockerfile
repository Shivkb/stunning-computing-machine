FROM python:3.7-alpine
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /mysite
WORKDIR /mysite
COPY ./mysite /mysite

RUN adduser -D ubuntu
USER ubuntu
