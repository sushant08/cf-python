FROM ubuntu:latest

COPY cf-flask.py .

RUN apt-get update \
  && apt-get install python  -y \
  && apt-get install -y python-pip \
  && pip install Flask

EXPOSE 5000
ENTRYPOINT ['python','cf-flask.py']

