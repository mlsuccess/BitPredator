import pandas as pd
import numpy as np

def ordered():
    df1 = pd.read_csv('https://raw.githubusercontent.com/lennymelnik/cryptoWinner/master/trans.csv',delimiter=';')
    od = {}
    ordates = []
    for i in range(len(df1['Date'].values)):
        od[df1['Date'].values[i]] = df1['Transactions'].values[i]
    for i in sorted(list(od.keys())):
        ordates.append(i)

    df2 = pd.read_csv('https://raw.githubusercontent.com/lennymelnik/cryptoWinner/master/coins.csv',delimiter=',')
    od2 = {}
    for i in range(len(df2['Date'].values)):
        od2[df2['Date'].values[i]] = df2['Close'].values[i]
    
    x = []
    y = []
    for i in ordates:
        if i in od2.keys():
            x.append(od2[i])
            y.append(od[i])
    return np.array(x), np.array(y)
x,y = ordered()
btcTrans = x
print(btcTrans)