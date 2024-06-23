import pandas as pd
import pandas_ta as ta
import requests

def get_data():
    url = "https://api-testnet.bybit.com/v5/market/kline"
    par = {"category": "spot",
           "symbol": "SOLUSDT",
           "interval": 60}
    response = requests.get(url, params = par)
    data = response.json()
    
    return data

def calculate_RSI(data, period = 14):
    
    columns = ["start_time", "open_price", "high_price", "low_price", "close_price", "volume", "turnover"]
    kline_list = data["result"]["list"]
    
    df = pd.DataFrame(kline_list, columns=columns)

    df["start_time"] = pd.to_datetime(df["start_time"], unit = "ms")
    df["open_price"] = df["open_price"].astype(float)
    df["high_price"] = df["high_price"].astype(float)
    df["low_price"] = df["low_price"].astype(float)
    df["close_price"] = df["close_price"].astype(float)
    df["volume"] = df["volume"].astype(float)
    df["turnover"] = df["turnover"].astype(float)

    df.set_index("start_time", inplace = True)
    df = df.sort_index(ascending = True)

    RSI_df = pd.DataFrame(df["close_price"])
    RSI = RSI_df.ta.rsi(length = period, append=True)
    print(RSI)

    return RSI[-1]

print(calculate_RSI(get_data()))