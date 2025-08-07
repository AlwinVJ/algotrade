import yfinance as yf

# Function to fecth stock data using yfinance

def fetch_stock_data(ticker, period="6mo",interval="1d"):
    data = yf.download(ticker, period = period, interval=interval)
    data.rename(columns={'Close': 'ClosePrice'}, inplace=True) #Renamed Close to ClosePrice to get be more accurate
    return data

# if __name__ == "__main__":
#     df = fetch_stock_data("TCS.NS")
#     print(df.head())