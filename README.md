# Flight Data Batch Processing Pipeline

Overview

  This project is a local microservices-based data processing system built to handle batch ingestion, processing, and delivery of flight data. It demonstrates a modular, scalable, and maintainable architecture using Docker containers.

Microservices

1. Ingestion Service

  Language: Python
  
  Function: Reads raw flight data (CSV), cleans, and loads into PostgreSQL
  
  Technologies: pandas, SQLAlchemy

2. Processing Service

  Language: Python with PySpark
  
  Function: Reads raw data, aggregates CO2 emissions per route by quarter and year
  
  Technologies: PySpark, PostgreSQL JDBC

3. Delivery Service

  Language: Python with Flask
  
  Function: Exposes aggregated data via REST API
  
  Endpoint: /aggregated-flights
  
  Supports query params: year, quarter

Setup Instructions

  1. Clone the repository:
    git clone https://github.com/yourusername/flight-data-pipeline.git
    cd flight-data-pipeline
  
  2. Create .env files for each microservice (use example provided in each folder).
     
  3. Run the services using Docker Compose:
     docker-compose up --build -d
     
  4. Access the API:
     http://localhost:5002/aggregated-flights

Features

  Clean ETL pipeline using microservices
  
  Docker-based reproducibility
  
  Environment separation for credentials
  
  Query API for insights on flight emissions
