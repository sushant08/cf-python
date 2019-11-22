FROM ubuntu:latest

COPY app.py .

RUN apt-get update \
  && apt-get install python  -y \
  && apt-get install -y python-pip \
  && pip install Flask

EXPOSE 5000
ENTRYPOINT ['python','app.py']

