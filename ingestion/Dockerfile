# Dockerfile for ingestion microservice
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y \
    gcc \
    g++ \
    build-essential \
    libmariadb-dev-compat \
    libmariadb-dev \
    pkg-config \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --default-timeout=600 -r requirements.txt

CMD ["python", "main.py"]
