FROM ubuntu:latest

COPY app.py .
COPY version .

RUN apt-get update \
  && apt-get install python  -y \
  && apt-get install -y python-pip \
  && pip install Flask

WORKDIR .

EXPOSE 5000
ENTRYPOINT ['python','app.py']

