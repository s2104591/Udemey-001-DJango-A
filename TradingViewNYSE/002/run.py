import ETRADE_TradingTA as toolsTA

doEtrade=True

if doEtrade:
    #toolsTA.get_Etrade_Individually(maxcount=300)

    strresult,dfresult= toolsTA.Go(incEtrade=True, incNASDAQ=True, incNYSE=True, maxcount=40, savefile="Recommend-Oct27.csv",method=2)
    print(strresult)
    print(dfresult.head(20))


else:

    reccomend1=toolsTA.get_Summary_Single(symbol="RL", screener='america',exchange="NYSE")
    reccomend2=toolsTA.get_Summary_Single(symbol="MIN", screener='australia',exchange="ASX")

    strresult,dfresult= toolsTA.Go(incEtrade=False, incNASDAQ=True, incNYSE=True, maxcount=40, savefile="Recommend-Oct25.csv",method=2)



    print(reccomend1,"\n",reccomend2)
    print(strresult)
    print(dfresult.head(20))



#print("\n\nhello Mariano Rico. Started the course Sept 28, 2023")