from plotGraph import graphTwo
from btcTrends import btcInterest
from btcStats import btcOpen
from btcTrans import btcTrans


graphTwo(btcTrans,btcOpen, "Price", "Transactions")


#Google trends and bitcoin price over time (Dates may not be in order in the google trends list)
graphTwo(btcOpen[:261],btcInterest, "Trend" ,"Price")
