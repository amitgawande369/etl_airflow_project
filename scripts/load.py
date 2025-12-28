import pandas as pd
from sqlalchemy import create_engine

DB_PATH = "database/etl.db"

def load_data():
    engine = create_engine(f"sqlite:///{DB_PATH}")

    df = pd.read_csv("data/processed/final_data.csv")

    df.to_sql("etl_data", engine, if_exists="replace", index=False)

    print("✅ Data loaded into SQLite database")
