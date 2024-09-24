FROM python:3.11-slim-bookworm
LABEL version=0.1

USER root

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY flag.txt /app/flag.txt
COPY app.py /app/app.py

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]