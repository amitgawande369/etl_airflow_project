from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    description="ETL Pipeline with CSV, JSON, API to SQLite/PostgreSQL",
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract_data
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform_data
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load_data
    )

    extract_task >> transform_task >> load_task
