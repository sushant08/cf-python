FROM ubuntu:latest

COPY cf-flask.py .

RUN apt-get update \
  && apt-get install python3 \
  && apt-get install -y python3-pip \
  && pip3 install Flask

EXPOSE 5000
ENTRYPOINT ['python3','cf-flask.py']

