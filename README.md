# Kalimati Market Price Scraper

A Python script that automatically fetches daily commodity prices from the Kalimati Market API (Nepal) and saves them in multiple formats (CSV, Excel, JSON) with proper directory structure.

## Features

- Fetches prices in both English and Nepali languages
- Saves data in multiple formats: CSV, Excel, and JSON
- Organized file structure by date (YYYY/MM/DD)
- Automatic directory creation
- Clean column naming for better readability
- Scheduled daily execution support

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Required Dependencies

Install the required packages using pip:

\`\`\`bash
pip install requests pandas openpyxl schedule
\`\`\`

Or create a `requirements.txt` file:

\`\`\`txt
requests>=2.25.0
pandas>=1.3.0
openpyxl>=3.0.0
schedule>=1.1.0
\`\`\`

Then install with:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Usage

### Instant Run

To fetch prices immediately and save them:

\`\`\`bash
python kalimati_scrape.py
\`\`\`

This will:
- Fetch current day prices in both English and Nepali
- Save data in `data/csv/`, `data/excel/`, and `data/json/` directories
- Create organized folder structure by year/month

### Scheduled Run (Cron Job)

To run the scraper automatically every day at 7:00 AM:

\`\`\`bash
python cron_job.py
\`\`\`

This will:
- Start a scheduler that runs in the background
- Execute the scraper daily at 7:00 AM
- Keep running until manually stopped (Ctrl+C)

## File Structure

After running the scraper, your directory structure will look like:

\`\`\`
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
\`\`\`

## Data Format

The scraped data includes the following columns:

- **Date**: Date of the price data
- **Commodity**: Name of the commodity
- **Unit**: Unit of measurement
- **Minimum**: Minimum price
- **Maximum**: Maximum price  
- **Average**: Average price

### Sample CSV Output

\`\`\`csv
Date,Commodity,Unit,Minimum,Maximum,Average
2025-08-27,Rice,Kg,45.0,55.0,50.0
2025-08-27,Wheat,Kg,35.0,40.0,37.5
\`\`\`

### Sample JSON Output

\`\`\`json
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
\`\`\`

## API Information

- **Source**: Kalimati Market Government API
- **Endpoint**: `https://kalimatimarket.gov.np/api/daily-prices`
- **Languages**: English (`en`) and Nepali (`np`)
- **Data**: Daily commodity prices from Kalimati Market, Nepal

## Functions Overview

### Core Functions

- `path_checker(path)`: Creates directories if they don't exist
- `file_name(date_str, output)`: Generates organized file paths
- `get_prices(lang)`: Fetches price data from API
- `save_csv()`, `save_excel()`, `save_json()`: Save data in respective formats

### Scheduler Functions

- `job()`: Wrapper function for scheduled execution
- Daily scheduling at 7:00 AM using the `schedule` library

## Error Handling

The script includes basic error handling:
- HTTP request errors are raised using `requests.raise_for_status()`
- Directory creation is handled with `exist_ok=True`
- UTF-8 encoding ensures proper character handling for Nepali text

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the API terms of service for the Kalimati Market API usage guidelines.

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure all dependencies are installed
2. **Permission Error**: Ensure write permissions in the project directory
3. **Network Error**: Check internet connection and API availability
4. **Encoding Issues**: The script uses UTF-8 encoding for proper Nepali character support

### Support

If you encounter any issues, please check:
- Python version compatibility
- All dependencies are properly installed
- API endpoint is accessible
- Sufficient disk space for data storage
