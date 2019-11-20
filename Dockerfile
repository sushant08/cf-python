FROM ubuntu:latest

COPY cf-flask.py .

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && pip3 install flask

EXPOSE 5000
ENTRYPOINT ['python','cf-flask.py']

