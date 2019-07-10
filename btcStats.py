import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

names = ['Date','Symbol', 'Open', 'Close', 'Volume BTC', 'Volume USD']
url = 'http://www.cryptodatadownload.com/cdd/Coinbase_BTCUSD_d.csv'
df = pd.read_csv(url, skiprows=[0,1], header = None, delim_whitespace = True, na_values='?')
df = df.replace(","," ", regex = True)
new = df[0].str.split(" ", n=7, expand=True)
df["Date"] = new[0]
df["Symbol"] = new[1]
df["Open"] = new[2]
df["High"] = new[3]
df["Low"] = new[4]
df["Close"] = new[5]
df["Volume BTC"] = new[6]
df["Volume USD"] = new[7]
y = df.head(100)["Open"]
x = df.head(100)["Date"]
y = pd.to_numeric(y)
btcOpen = pd.to_numeric(df.head(352)["Open"])
btcOpenDate = df.head(352)["Date"]
plt.plot(x,y,'o')
#Flip the values so date is going from back to front
plt.gca().invert_xaxis()
plt.xlabel("Date")
plt.ylabel("Open")
plt.grid()

plt.show()
print(new[0])