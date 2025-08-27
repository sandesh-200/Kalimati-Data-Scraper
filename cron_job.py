import schedule
import time
from kalimati_scrape import main

def job():
    print("🕖 Running daily Kalimati scraper...")
    main()

# Schedule the job every day at 07:00 AM
schedule.every().day.at("07:00").do(job)

print("⏰ Scheduler started. Waiting for 7 AM daily...")

while True:
    schedule.run_pending()
    time.sleep(30)
