from utils import *
import time, datetime

df = pd.read_csv('coins.csv')
print(df['Date'].values)

from pytrends.request import TrendReq
data = {}
for term in ['bitcoin','coinbase']:
    trends = TrendReq(hl='en-US', tz=360)
    trends.build_payload([term],timeframe='today 3-m')
    iot = trends.interest_over_time()
    data['gt-'+term] = {}
    print(iot.columns)
    for i in range(len(iot[term].values)):
        d = datetime.date.today()-datetime.timedelta(days=89-i)
        data['gt-'+term][d.isoformat()] = iot[term].values[i]

df = pd.read_csv('coins.csv')
for i in ['Close','High','Low']:
    data['bt-'+i] = {}
    c = 0
    for x in df[i].values:
        data['bt-'+i][df['Date'].values[c]] = x
        c += 1

df = pd.read_csv('weatherHistory.csv')
ld = None
for i in ['Temperature (C)','Apparent Temperature (C)','Humidity']:
    data['w-'+i] = {}
    for x in range(len(df[i].values)):
        if df['Formatted Date'].values[x].split(' ')[0] != ld:
            ld = df['Formatted Date'].values[x].split(' ')[0]
            data['w-'+i][ld] = df[i].values[x]
print(data['w-Humidity'])



    

