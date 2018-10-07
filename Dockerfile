FROM python:3.6-alpine
MAINTAINER Caian R. Ertl <caianrais@pm.me>

WORKDIR app
COPY setup.py dora ./

RUN python3 setup.py build
RUN python3 setup.py install

EXPOSE 80
ENTRYPOINT python3 dora.py start --port 80
