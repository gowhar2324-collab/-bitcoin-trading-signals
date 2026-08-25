import yfinance as yf
import pandas as pd

# Bitcoin weekly data
btc = yf.download("BTC-USD", period="2y", interval="1wk", auto_adjust=True)

# Calculate indicators
btc["SMA_20"] = btc["Close"].rolling(20).mean()
btc["SMA_50"] = btc["Close"].rolling(50).mean()

# Get latest values
price = float(btc["Close"].iloc[-1])
sma20 = float(btc["SMA_20"].iloc[-1])
sma50 = float(btc["SMA_50"].iloc[-1])

# Generate weekly signal
if price > sma20 and sma20 > sma50:
    signal = "BUY"
elif price < sma20 and sma20 < sma50:
    signal = "SELL"
else:
    signal = "HOLD"

print("Bitcoin Weekly Trading Signal")
print("-----------------------------")
print(f"Price: ${price:,.2f}")
print(f"SMA 20: ${sma20:,.2f}")
print(f"SMA 50: ${sma50:,.2f}")
print(f"Signal: {signal}")
