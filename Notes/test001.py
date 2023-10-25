
from tradingview_ta import TA_Handler, Interval, Exchange
import pandas as pd
import datetime

from tradingview_ta import *



def get_multiple(maxcount=10):
    printTimeStr()
    codes=get_Nasdaq()
    naslist=[]
    count=0 
    
    for c in codes:
        naslist.append("nasdaq:"+c)
        count+=1
        if count==maxcount:
            break


    #print(naslist)    

    analysis = get_multiple_analysis(screener="america", interval=Interval.INTERVAL_1_HOUR,\
        symbols=naslist)
        #symbols=["nasdaq:AAL", "nasdaq:AAOI", "nasdaq:AAON", "nasdaq:AAPL", "nasdaq:ABCB",\
        #        "nasdaq:ABCL", "nasdaq:ABCM", "nasdaq:ABNB", "nasdaq:ACAD", "nasdaq:ACAH"])

    printTimeStr()
    return analysis 


def get_RSI(symbol="TSLA", screener='america',exchange="NASDAQ"):
    tesla=TA_Handler(
        symbol=symbol,
        screener=screener,
        exchange= exchange,
        interval=Interval.INTERVAL_1_MINUTE
    )


    #tesla.get_analysis().summary
    result= tesla.get_analysis().indicators['RSI'] 
    return result

def get_Nasdaq():
    df=pd.read_csv("nasdaq-Oct25.csv") 
    result= list( df.Symbol )

    return result

def printTimeStr():
    # Get the current date and time
    current_time = datetime.datetime.now()

    # Format the current time as a string
    strTime = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("\n","*** TIME=",strTime,"\n")  



def get_All():
    codes=get_Nasdaq()
    count=0
    printTimeStr()

    for c in codes:
        code="TSLA"
        rsi= get_RSI(symbol=c) 
        print(c, "RSI=",rsi)
        
        count+=1
        if count>=10:
            break

    printTimeStr()

def getCode(key):
    colindex=key.find(":")+1
    return key[colindex:]    


def Go():

    maxamt=995
    mydict=get_multiple(maxcount=maxamt)

    code_list=[]
    val_list=[]

    count=0
    for k in mydict:
        val=mydict[k]
        if val != None:
            val=mydict[k].indicators['RSI']
            code=getCode(k)

            val_list.append(val)
            code_list.append(code)
            
            #print(count,k,code ,val)
        count+=1

    df=pd.DataFrame( {"Code":code_list, "RSI":val_list }) 
    df_sorted = df.sort_values(by=['RSI', 'Code'], ascending=[False, True])
    return df_sorted

df= Go()

print(df.head(20) )








print("hello Mariano Rico. Started the course Sept 28, 2023")
