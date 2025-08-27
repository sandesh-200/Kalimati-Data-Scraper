# Kalimati Market Price Scraper

A Python script that automatically fetches daily commodity prices from the **Kalimati Market API (Nepal)** and saves them in multiple formats (CSV, Excel, JSON) with a neat directory structure.

---

## Features

- Fetches prices in **English** and **Nepali**  
- Saves data in multiple formats: **CSV**, **Excel**, **JSON**  
- Organized directory structure by date (`YYYY/MM/DD`)  
- Automatic folder creation  
- Clean and readable column names  
- Supports **scheduled daily execution**

---

## Installation 🛠️

### Prerequisites

- Python 3.7 or higher  
- pip package manager  

### Install Dependencies

**Option 1: Install via pip**

```bash
pip install requests pandas openpyxl schedule
```

**Option 2: Using `requirements.txt`**

```txt
requests>=2.25.0
pandas>=1.3.0
openpyxl>=3.0.0
schedule>=1.1.0
```

Then run:

```bash
pip install -r requirements.txt
```

---

## Usage

### Instant Run

To fetch prices immediately:

```bash
python kalimati_scrape.py
```

This will:

- Fetch current day prices in **English & Nepali**  
- Save data in:
  - `data/csv/`
  - `data/excel/`
  - `data/json/`  
- Automatically create **year/month folders**

---

### Scheduled Run (Cron Job)

To run the scraper daily at **7:00 AM**:

```bash
python cron_job.py
```

This will:

- Start a scheduler running in the background  
- Execute the scraper daily at 7:00 AM  
- Keep running until manually stopped (`Ctrl+C`)

---

## File Structure

After running the scraper:

```
project/
├── kalimati_scrape.py
├── cron_job.py
├── README.md
└── data/
    ├── csv/
    │   └── 2025/
    │       └── 08/
    │           └── 27.csv
    ├── excel/
    │   └── 2025/
    │       └── 08/
    │           └── 27.xlsx
    └── json/
        └── 2025/
            └── 08/
                └── 27.json
```

---

## Data Format

Columns:

- **Date**: Date of the price data  
- **Commodity**: Name of the commodity  
- **Unit**: Unit of measurement  
- **Minimum**: Minimum price  
- **Maximum**: Maximum price  
- **Average**: Average price  

### Sample CSV

```csv
Date,Commodity,Unit,Minimum,Maximum,Average
2025-08-27,Rice,Kg,45.0,55.0,50.0
2025-08-27,Wheat,Kg,35.0,40.0,37.5
```

### Sample JSON

```json
{
  "Date": "2025-08-27",
  "prices": [
    {
      "Commodity": "Rice",
      "Unit": "Kg",
      "Minimum": 45.0,
      "Maximum": 55.0,
      "Average": 50.0
    }
  ]
}
```

---

## API Information

- **Source**: Kalimati Market Government API  
- **Endpoint**: `https://kalimatimarket.gov.np/api/daily-prices`  
- **Languages**: English (`en`) & Nepali (`np`)  
- **Data**: Daily commodity prices from Kalimati Market, Nepal

---

## Functions Overview 🛠️

### Core Functions

- `path_checker(path)`: Creates directories if not exist  
- `file_name(date_str, output)`: Generates organized file paths  
- `get_prices(lang)`: Fetches price data from API  
- `save_csv()`, `save_excel()`, `save_json()`: Save data in respective formats  

### Scheduler Functions

- `job()`: Wrapper function for scheduled execution  
- Uses `schedule` library to run daily at **7:00 AM** 

---

## License

Open source. Please check the API terms of service for Kalimati Market API usage guidelines.

---

