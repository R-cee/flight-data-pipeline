# Dockerfile for Flask delivery microservice
FROM python:3.9-slim

WORKDIR /app

COPY . .

# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --default-timeout=600 -r requirements.txt


EXPOSE 5002

CMD ["python", "main.py"]
