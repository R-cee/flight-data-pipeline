FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y default-jdk procps && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --default-timeout=600 pyspark==3.5.0 pandas python-dotenv

ENV JAVA_HOME=/usr/lib/jvm/default-java

CMD ["python", "main.py"]
