import os
import json
import requests
import pandas as pd
from datetime import datetime

API_URL = "https://kalimatimarket.gov.np/api/daily-prices"
LANGS = ["en", "np"]  # English & Nepali

# -----------------------------
# Helpers
# -----------------------------

def path_checker(path: str):
    """Make sure directory exists"""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def file_name(date_str: str, output: str) -> str:
    """Generate file path like data/csv/2025/08/27.csv"""
    year, month, day = date_str.split("-")
    dir_path = f"data/{output}/{year}/{month}"
    path_checker(dir_path)
    ext_map = {"csv": "csv", "json": "json", "excel": "xlsx"}
    return f"{dir_path}/{day}.{ext_map[output]}"


# -----------------------------
# Converters (with renamed columns)
# -----------------------------

def save_csv(data, date_str):
    file = file_name(date_str, "csv")
    df = pd.DataFrame(data["prices"])
    df.insert(0, "Date", data["date"])
    
    # Rename columns
    df = df.rename(columns={
        "commodityname": "Commodity",
        "commodityunit": "Unit",
        "minprice": "Minimum",
        "maxprice": "Maximum",
        "avgprice": "Average"
    })
    
    df.to_csv(file, index=False, encoding="utf-8")
    print(f"✅ CSV saved: {file}")


def save_excel(data, date_str):
    file = file_name(date_str, "excel")
    df = pd.DataFrame(data["prices"])
    df.insert(0, "Date", data["date"])
    
    # Rename columns
    df = df.rename(columns={
        "commodityname": "Commodity",
        "commodityunit": "Unit",
        "minprice": "Minimum",
        "maxprice": "Maximum",
        "avgprice": "Average"
    })
    
    df.to_excel(file, index=False, engine="openpyxl")
    print(f"✅ Excel saved: {file}")


def save_json(data, date_str):
    file = file_name(date_str, "json")
    prices = []
    for item in data["prices"]:
        prices.append({
            "Commodity": item["commodityname"],
            "Unit": item["commodityunit"],
            "Minimum": item["minprice"],
            "Maximum": item["maxprice"],
            "Average": item["avgprice"]
        })
    output = {"Date": data["date"], "prices": prices}
    with open(file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"✅ JSON saved: {file}")


# -----------------------------
# Fetching Logic
# -----------------------------

def get_prices(lang: str):
    url = f"{API_URL}/{lang}"
    resp = requests.get(url, headers={"Content-Type": "application/json"})
    resp.raise_for_status()
    return resp.json()


# -----------------------------
# Main Function
# -----------------------------

def main():
    for lang in LANGS:
        print(f"\n📦 Fetching prices in {lang.upper()}...")
        data = get_prices(lang)

        date_str = data["date"]

        # Save into all formats
        save_csv(data, date_str)
        save_excel(data, date_str)
        save_json(data, date_str)

    print("\n🎉 All done!")


if __name__ == "__main__":
    main()
