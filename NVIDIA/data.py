import datetime as dt
import pandas as pd
import yfinance as yf

start = "2010-01-01"
end = dt.date.today().isoformat() 

df = yf.download(
    "NVDA",
    start=start,
    end=end,
    interval="1d",
    auto_adjust=True,   
    progress=False,
)

csv_path = f"nvda_data.csv"
df.to_csv(csv_path)

csv_path
