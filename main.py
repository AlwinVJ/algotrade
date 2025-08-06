from stock_data import fetch_stock_data
from trade_strategy import buy_signal, apply_indicators

df = fetch_stock_data('TCS.NS')
df = apply_indicators(df)
df = buy_signal(df)
print(df.tail())