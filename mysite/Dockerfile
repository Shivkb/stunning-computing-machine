FROM python:3.7-alpine
ENV PYTHONBUFFERED 1
ENV deployment docker
RUN apk add --no-cache bash
RUN apk add --update  --no-cache postgresql-client
RUN apk add --update  --no-cache --virtual .tmp-build-deps \
     gcc libc-dev linux-headers postgresql-dev

RUN mkdir /mysite
RUN mkdir /db
COPY ./requirements.txt /mysite/
COPY ./manage.py /mysite/
RUN pip install -r /mysite/requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir -p /mysite/mysite
RUN mkdir -p /var/log
RUN chmod uog+rwx /var/log
WORKDIR /mysite
COPY ./mysite /mysite/mysite
COPY ./core /mysite/core
COPY ./user /mysite/user

RUN adduser -D ubuntu
USER ubuntu
