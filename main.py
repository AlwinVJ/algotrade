from stock_data import fetch_stock_data
from trade_strategy import buy_signal, apply_indicators
from backtest import stock_backtest

df = fetch_stock_data('WIPRO.NS')
df = apply_indicators(df)
df = buy_signal(df)
print(df.tail())

trade_log, summary = stock_backtest(df)

print("Trade Logs", trade_log)
print("Summary",summary)
