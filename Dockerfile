# syntax=docker/dockerfile:1

FROM python:3.9.6-slim-buster

RUN apt-get update && apt-get install -y \
  python-pyramid

WORKDIR /app
COPY . .
RUN pip3 install -e .