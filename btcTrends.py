import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
import datetime
from dateutil.parser import parse
from btcTrans import ordered
from pytrends.request import TrendReq
from plotGraph import graphTwo

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Bitcoin"]
print(pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop=''))
btcInterest = pytrends.interest_over_time()
btcInterest = btcInterest['Bitcoin']
print(btcInterest)
