FROM python:3.6

VOLUME /app

WORKDIR /app

COPY *.py /app/
COPY requirements.txt /app/

RUN apt update \
    && apt upgrade

COPY packages.txt /app/packages.txt

RUN apt install -y $(awk '{print $1}' /app/packages.txt) \
    && apt clean

RUN pip install -r requirements.txt
