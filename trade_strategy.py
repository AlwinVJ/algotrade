# Trading Strategy Logic:
# Implement RSI < 30 as a buy signal
# Confirm with 20-DMA crossing above 50-DMA

import ta

def apply_indicators(df):
    # Calculating the RSI for stock's closing price, storing it in rsi column
    df['rsi'] = ta.momentum.RSIIndicator(close = df['ClosePrice'].squeeze()).rsi()
    df['ma20'] = df['ClosePrice'].rolling(window=20).mean() #Calculates the 20 Days moving average(DMA)
    df['ma50'] = df['ClosePrice'].rolling(window = 50).mean() #Calculates the 50 DMA
    
    return df

def buy_signal(df):
    signals = []
    for i in range(1, len(df)):
        # if df['rsi'][i] < 30 and df['ma20'][i]>df['ma50'][i] and df['ma20'][i-1] <= df['ma50'][i-1]:
        if df['rsi'].iloc[i] < 30 and df['ma20'].iloc[i] > df['ma50'].iloc[i] and df['ma20'].iloc[i-1] <= df['ma50'].iloc[i-1]:
            signals.append("BUY")
        else:
            signals.append("NO ADVICE")
    signals.insert(0,"")
    df['Signal'] = signals
    return df
    