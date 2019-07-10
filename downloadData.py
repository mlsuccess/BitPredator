import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
import datetime
from dateutil.parser import parse
from parse import ordered
from pytrends.request import TrendReq

#Prices
names = ['Date','Symbol', 'Open', 'Close', 'Volume BTC', 'Volume USD']
url = 'http://www.cryptodatadownload.com/cdd/Coinbase_BTCUSD_d.csv'
df = pd.read_csv(url, skiprows=[0,1], header = None, delim_whitespace = True, na_values='?')
#Transactions Dataframe
names2 = ['Date','Transactions']
url2 = 'https://raw.githubusercontent.com/lennymelnik/cryptoWinner/master/trans.csv'
df1 = pd.read_csv(url2, header = None, delim_whitespace = True, na_values='?')
"""print(df1)"""
#x = df['Open'].values
#df.dropna(inplace = True)
#df = pd.DataFrame(df[0])
df = df.replace(","," ", regex = True)
new = df[0].str.split(" ", n=7, expand=True)
df1 = df1.replace(","," ", regex = True)
new1 = df1[0].str.split(" ", n=7, expand=True)
print(df1)
df1["Other"] = new[3]
df1["Date"] = new[1]
df1["Transactions"] = new[2]
df["Date"] = new[0]
df["Symbol"] = new[1]
df["Open"] = new[2]
df["High"] = new[3]
df["Low"] = new[4]
df["Close"] = new[5]
df["Volume BTC"] = new[6]
df["Volume USD"] = new[7]
x = df1.head(100)["Other"]
#x = pd.to_numeric(x)
#x = [time.mktime(datetime.datetime.strptime(, "%d/%m/%Y").timetuple()) for g in x]
y = df.head(100)["Open"]
y = pd.to_numeric(y)
print(x)
print(y)

#plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.plot(x,y,'o')
#Flip the values so date is going from back to front
plt.gca().invert_xaxis()
print("Test2")
plt.xlabel("Date")
plt.ylabel("Open")
plt.grid()

plt.show()

#print (df["Open"])
def findAll(x, y):
    meanx = np.mean(x)
    meany = np.mean(y)
    varx = np.var(x)
    vary = np.var(y)
    covxy = np.mean((x - meanx) * (y - meany))
    rho = covxy / (np.sqrt(varx * vary))
    bestY = (meany + rho * (np.sqrt(vary)/np.sqrt(varx))*(x - meanx))
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
    plt.ylim(min(y)-10,max(y)+10)
    plt.plot(x, y, 'o')
    plt.plot(x, bestY)
    plt.xlabel("Transactions")
    plt.ylabel("Price")
    plt.grid()

    # Find all the unique points and those shall be the x values, for y it will be th
    plt.show()


x, y = ordered()
print(len(x))
findAll(x,pd.to_numeric(df.head(352)["Open"]))

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Bitcoin"]
print(pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop=''))
btcInterest = pytrends.interest_over_time()
btcInterest = btcInterest['Bitcoin']
print(btcInterest)
findAll(x,btcInterest)



