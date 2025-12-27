import pandas as pd

def transform_weather():
    df = pd.read_csv("/tmp/weather_raw.csv")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["temperature"] = df["temperature"].fillna(df["temperature"].mean())

    df.to_csv("/tmp/weather_transformed.csv", index=False)
