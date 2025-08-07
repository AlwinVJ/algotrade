from stock_data import fetch_stock_data
from trade_strategy import apply_indicators, buy_signal
from backtest import stock_backtest
from googlesheets import authorize_google_sheets, upload_dataframe, upload_summary

# 1. Fetch and process data
df = fetch_stock_data("TATAMOTORS.NS")
df = apply_indicators(df)
df = buy_signal(df)

# 2. Run backtest and get trade_log and summary
trade_log, summary = stock_backtest(df)

# 3. Authorize Google Sheets and upload data
client = authorize_google_sheets("creds.json")
sheet = client.open("AlgoTradingLog")

# print("Trade Log shape:", trade_log.shape)
# print(trade_log.head())

# print("Summary:", summary)

# 4. Upload to respective tabs
upload_dataframe(sheet, trade_log, "Trade Log")
upload_summary(sheet, summary, "Trade Summary")

