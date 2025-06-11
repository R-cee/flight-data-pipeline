# Flight Data Batch Processing Pipeline

Overview

  This project is a local microservices-based data processing system built to handle batch ingestion, processing, and delivery of flight data. It demonstrates a modular, scalable, and maintainable architecture using Docker container, Airflow orchestration, and REST APIs.

  It performs ETL on raw flight data, aggregates CO2 emissions per route by quarter and year, and exposes the aggregated data via a REST API or downloadable CSV file.

Microservices

1. Ingestion Service

  Language: Python
  
  Function: Reads raw flight data (CSV), cleans, and loads into PostgreSQL
  
  Technologies: pandas, SQLAlchemy

2. Processing Service

  Language: Python with PySpark
  
  Function: Reads raw data, aggregates CO2 emissions per route by quarter and year, using Spark for distributed processing
  
  Technologies: PySpark, PostgreSQL JDBC

3. Delivery Service

  Language: Python with Flask
  
  Function: Exposes aggregated data via REST API or as downloadable CSV file
  
  Endpoint: /aggregated-flights
  
  Supports query params: year, quarter, format=json|csv

Setup Instructions

  1. Clone the repository:
    git clone https://github.com/R-cee/flight-data-pipeline.git
    cd flight-data-pipeline
  
  2. Create .env files for each microservice (use example provided in each folder).
     
  3. Run the services using Docker Compose:
     docker-compose up --build -d

  4. Initialize Airflow Database (one-time step)
     docker-compose run --rm airflow-webserver airflow db init

  6. Create Airflow Admin User (one-time step):

    docker-compose run --rm airflow-webserver airflow users create `
    --username airflow `
    --password airflow `
    --firstname Airflow `
    --lastname Admin `
    --role Admin `
    --email airflow.admin@gmail.com

  6. Access the Airflow Web UI:

    http://localhost:8080

    Login using the credentials you just created
    
    Trigger the flight_data_pipeline DAG manually or set it to run on schedule
     
  7. Access the API for aggregated data:
     
    http://localhost:5002/aggregated-flights
       
    JSON Response:
    http://localhost:5002/aggregated-flights?year=2022&quarter=2

    CSV Download:
    http://localhost:5002/aggregated-flights?year=2022&quarter=2&format=csv
  

Features

    Clean ETL (Extract, Transform, Load) pipeline using Dockerized microservices
  
    Scalable architecture using Airflow orchestration

    REST API and CSV support for reporting

    Docker-based reproducibility
  
    Environment separation for credentials
  
    Query API for insights on flight emissions
