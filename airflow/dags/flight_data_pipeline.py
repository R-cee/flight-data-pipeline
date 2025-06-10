from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'flight_data_pipeline',
    default_args=default_args,
    description='A DAG to orchestrate flight data ingestion, processing, and delivery',
    schedule_interval='@monthly',
    catchup=False,
)

docker_common_args = {
    'api_version': 'auto',
    'auto_remove': True,
    'docker_url': 'unix://var/run/docker.sock',
    'network_mode': 'flight-data-pipeline_default',  
    'mount_tmp_dir': False, 
}

ingest = DockerOperator(
    task_id='run_ingestion',
    image='flight-data-pipeline-ingestion',
    command='python main.py',
    dag=dag,
    **docker_common_args
)

process = DockerOperator(
    task_id='run_processing',
    image='flight-data-pipeline-processing',
    command='python main.py',
    dag=dag,
    **docker_common_args,
    environment={
        "DB_HOST": "postgres",
        "DB_PORT": "5432",
        "DB_NAME": "flight_data",
        "DB_USER": "postgres",
        "DB_PASSWORD": "yourpassword"
    }
)

deliver = DockerOperator(
    task_id='run_delivery',
    image='flight-data-pipeline-delivery',
    command='python main.py',
    dag=dag,
    **docker_common_args
)

ingest >> process >> deliver
