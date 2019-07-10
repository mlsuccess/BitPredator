import pandas as pd
import numpy as np
import matplotlib as mplt
import matplotlib.pyplot as plt

def stats(x,y,scase=None,case=None):
    if scase != None:
        x = x[case==scase]
        y = y[case==scase]
    xvar = np.sqrt(np.var(x))
    xmean =np.mean(x)
    yvar = np.sqrt(np.var(y))
    ymean =np.mean(y)
    cov = np.mean((x-xmean)*(y-ymean))
    cor = cov/(xvar*yvar)
    rho = cov / (np.sqrt(xvar * yvar))
    by = (ymean + rho * (np.sqrt(yvar)/np.sqrt(xvar))*(x - xmean))
    return {'mean':[xmean,ymean],'var':[xvar,yvar],'cov':cov,'cor':cor,'rho':rho,'by':by}