# syntax=docker/dockerfile:1

FROM python:3.9.6-slim-buster

RUN apt-get update && apt-get install -y \
  python-pyramid \
  sqlite3

WORKDIR /app
COPY . .
RUN pip3 install -e .
RUN sqlite3 simple_blog.sqlite
RUN chmod +x prod.sh