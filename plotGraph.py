import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
import datetime
from dateutil.parser import parse
from btcTrans import ordered
from pytrends.request import TrendReq

def graphTwo(x, y, yaxis, xaxis):
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
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.grid()

    # Find all the unique points and those shall be the x values, for y it will be th
    plt.show()