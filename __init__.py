from utils import *
import time, datetime

df = pd.read_csv('coins.csv')
print(df['Date'].values)

from pytrends.request import TrendReq
trends = TrendReq(hl='en-US', tz=360)
trendlist = {}
start = datetime.date.today()-datetime.timedelta(days=1821)
end = datetime.date.today()-datetime.timedelta(days=1821-i-1)
trends.build_payload(['bitcoin'],timeframe=start.isoformat()+' '+end.isoformat())
iot = trends.interest_over_time()
print(iot)
trendlist[start.isoformat()] = iot['bitcoin'].values[0]
    

print(trendlist)
    

