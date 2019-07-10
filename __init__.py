from utils import *
import time, datetime

df = pd.read_csv('coins.csv')

from pytrends.request import TrendReq

trends = TrendReq(hl='en-US', tz=360)
trendlist = []

for i in range(1820):
    start = datetime.today()-datetime.timedelta(days=1820-i)
    end = datetime.today()-datetime.timedelta(days=1820-i-1)
    trendlist.append(trends.get_historical_interest(['bitcoin'],day_start=start.days,year_start=start.year))

