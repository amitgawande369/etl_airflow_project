from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.extract import extract_weather
from scripts.transform import transform_weather
from scripts.load import load_weather

default_args = {
    "owner": "airflow",
    "retries": 1
}

with DAG(
    dag_id="weather_etl_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id="extract_weather",
        python_callable=extract_weather
    )

    transform = PythonOperator(
        task_id="transform_weather",
        python_callable=transform_weather
    )

    load = PythonOperator(
        task_id="load_weather",
        python_callable=load_weather
    )

    extract >> transform >> load
