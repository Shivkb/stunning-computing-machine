FROM python:3.7-alpine
ENV PYTHONBUFFERED 1
ENV deployment docker
RUN apk add --no-cache bash
RUN apk add --update  --no-cache postgresql-client jpeg-dev
RUN apk add --update  --no-cache --virtual .tmp-build-deps \
     gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

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
COPY ./recipe /mysite/recipe

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN addgroup --system ubuntu && adduser --system ubuntu -G ubuntu
RUN chown -R ubuntu:ubuntu /vol/
RUN chmod -R 755 /vol/web
USER ubuntu
