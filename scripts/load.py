import pandas as pd
from sqlalchemy import create_engine

def load_weather():
    engine = create_engine(
        "postgresql://airflow:airflow@localhost:5432/weather_db"
    )

    df = pd.read_csv("/tmp/weather_transformed.csv")
    df.to_sql("weather_data", engine, if_exists="replace", index=False)
