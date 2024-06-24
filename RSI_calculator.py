import pandas as pd
import pandas_ta as ta


df = pd.DataFrame(columns = ["close"])

async def handle_data(msg, channel, period):
    global df
    data = msg["data"][0]
    timestamp = pd.to_datetime(data["timestamp"], unit="ms")
    kline = {
        "timestamp": timestamp,
        "close": float(data["close"]),
    }
    
    df.loc[timestamp] = kline["close"]

    if data['confirm']:
        print("K-line closed at", timestamp)
        while len(df)+1 < period:
            period -= 1
            if period < len(df)+1:
                channel.send(f"Period has been changed to {period} because there were too few records.")
            if period <= 2:
                channel.send(f"There were too few records to calculate RSI")
                break
        if len(df) + 1 > period:
            rsi = calculate_RSI(df, period)
            print(f"Calculated RSI: {rsi}")
            if rsi > 70:
                await channel.send(f"RSI is higher than 70! Current RSI: {rsi}")
            elif rsi < 30:
                await channel.send(f"RSI is lower than 30! Current RSI: {rsi}")
            else:
                await channel.send(f"(test) Current RSI: {rsi}")
            df = pd.DataFrame(columns = ["close"])

def calculate_RSI(data, period = 14):
    RSI = data.ta.rsi(length = period, append=True)
    print(RSI)

    return float(RSI[-1])
