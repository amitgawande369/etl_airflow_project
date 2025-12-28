import pandas as pd
import os

RAW_DATA_PATH = "data/raw"
PROCESSED_DATA_PATH = "data/processed"

def transform_data():
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    df_csv = pd.read_csv(f"{RAW_DATA_PATH}/csv_data.csv")
    df_json = pd.read_csv(f"{RAW_DATA_PATH}/json_data.csv")
    df_api = pd.read_csv(f"{RAW_DATA_PATH}/api_data.csv")

    # Combine all datasets
    df = pd.concat([df_csv, df_json, df_api], ignore_index=True)

    # Basic transformations
    df.drop_duplicates(inplace=True)
    df.fillna("Unknown", inplace=True)

    df.to_csv(f"{PROCESSED_DATA_PATH}/final_data.csv", index=False)
    print("✅ Data transformation completed")
