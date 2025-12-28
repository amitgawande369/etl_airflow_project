import pandas as pd
import requests
import os

RAW_DATA_PATH = "data/raw"

def extract_data():
    os.makedirs(RAW_DATA_PATH, exist_ok=True)

    # Extract CSV
    csv_df = pd.read_csv(f"{RAW_DATA_PATH}/sample.csv")

    # Extract JSON
    json_df = pd.read_json(f"{RAW_DATA_PATH}/sample.json")

    # Extract API data
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    api_df = pd.DataFrame(response.json())

    # Save extracted data
    csv_df.to_csv(f"{RAW_DATA_PATH}/csv_data.csv", index=False)
    json_df.to_csv(f"{RAW_DATA_PATH}/json_data.csv", index=False)
    api_df.to_csv(f"{RAW_DATA_PATH}/api_data.csv", index=False)

    print("✅ Data extraction completed")
