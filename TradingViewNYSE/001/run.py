import NYSE_TradingTA as toolsTA



reccomend=toolsTA.get_Summary_Single(symbol="BANC", screener='america',exchange="NYSE")
strresult,dfresult= toolsTA.Go(incNASDAQ=True, incNYSE=True, maxcount=40, savefile="Recommend-Oct25.csv",method=2)

print(reccomend)
print(strresult)
print(dfresult.head(20))



#print("\n\nhello Mariano Rico. Started the course Sept 28, 2023")