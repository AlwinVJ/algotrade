from stock_data import fetch_stock_data
from trade_strategy import apply_indicators
from backtest import stock_backtest
from googlesheets import authorize_google_sheets, upload_summary
from ml_model import build_model

import schedule
import time

def job():
    print("Running scheduled job...")

    df = fetch_stock_data("RELIANCE.NS")
    df = apply_indicators(df)
    df.columns = ['_'.join(filter(None, map(str, col))) for col in df.columns]  # Flatten MultiIndex

    trade_log, summary = stock_backtest(df)
    print("Trade log:\n", trade_log)
    print("Summary:\n", summary)

    client = authorize_google_sheets("creds.json")
    upload_summary(client, "AlogTradingLog", trade_log, summary)

    model, accuracy = build_model(df)
    print(f"ML Model Accuracy: {accuracy}%")

# ⏰ Schedule to run at 9:30 AM every day
schedule.every().day.at("09:30").do(job)

print("Scheduler started. Waiting for 09:30...")
while True:
    schedule.run_pending()
    time.sleep(60)
