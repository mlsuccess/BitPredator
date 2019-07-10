from plotGraph import graphTwo
from btcTrends import btcInterestBitcoin, btcInterestCoinbase, btcInterestTemperature
from btcStats import btcOpen
from btcTrans import btcTrans


graphTwo(btcTrans,btcOpen, "Price", "Transactions")


#Google trends and bitcoin price over time (Dates may not be in order in the google trends list)
graphTwo(btcInterestCoinbase,btcOpen[:261],"Price", "Coinbase Search" )
graphTwo(btcInterestBitcoin,btcOpen[:261],"Price", "Bitcoin Search" )
graphTwo(btcInterestTemperature, btcOpen[:261],"Price", "Temperature Search" )
