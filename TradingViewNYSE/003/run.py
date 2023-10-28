import NYSE_TradingTA as toolsTA



reccomend=toolsTA.get_Summary_Single(symbol="RL", screener='america',exchange="NYSE")
print(reccomend)



#strresult,dfresult= toolsTA.GoNYSE("Recommend-USA-Oct28.csv")
strresult,dfresult= toolsTA.GoEtrade("Recommend-AUS-Oct28.csv")


print(strresult)
print(dfresult.head(20))



#print("\n\nhello Mariano Rico. Started the course Sept 28, 2023")