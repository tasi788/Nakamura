FROM python:3.7-slim as builder
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

FROM builder
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
