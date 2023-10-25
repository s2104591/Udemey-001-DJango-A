
from tradingview_ta import TA_Handler, Interval, Exchange
import pandas as pd
import datetime

from tradingview_ta import *



def get_multiple_NYSE():
    codes=get_NYSE_Codes_Merged()
    
    return get_Multiple_GENERIC(exchange="NYSE",codes=codes)


def get_multiple_NASDAQ():
    codes=get_Nasdaq_Codes()
    return get_Multiple_GENERIC(exchange="nasdaq",codes=codes)

def get_Multiple_GENERIC(exchange="nasdaq", codes=['TSLA',"AAPL"]):

    printTimeStr()
    naslist=[]
    count=0 
    
    #maxcount=len(codes)


    for c in codes:
        if len(c)>=6:
            pass
        else:
            naslist.append(exchange+":"+c)
            
            #count+=1
            #if count==maxcount:
            #    break


    #print(naslist)    

    analysis = get_multiple_analysis(screener="america", interval=Interval.INTERVAL_1_MINUTE,\
        symbols=naslist)
        #symbols=["nasdaq:AAL", "nasdaq:AAOI", "nasdaq:AAON", "nasdaq:AAPL", "nasdaq:ABCB",\
        #        "nasdaq:ABCL", "nasdaq:ABCM", "nasdaq:ABNB", "nasdaq:ACAD", "nasdaq:ACAH"])

    printTimeStr()
    return analysis 



def fetchAnalysis_Single(symbol="TSLA", screener='america',exchange="NASDAQ"):
    # to find out which exchange:
    # https://tvdb.brianthe.dev/   
    tesla=TA_Handler(
        symbol=symbol,
        screener=screener,
        exchange= exchange,
        interval=Interval.INTERVAL_1_MINUTE
    )
    result= tesla.get_analysis()
    return result


def get_RSI_Single(symbol="TSLA", screener='america',exchange="NASDAQ"):

    #tesla.get_analysis().summary
    result= fetchAnalysis_Single(symbol,screener,exchange).indicators['RSI'] 
    return result


def get_SP400_Codes():
    return get_NYSE_Codes(filename="SP400-Oct25.csv")

def get_SP600_Codes():
    return get_NYSE_Codes(filename="SP600-Oct25.csv")

def get_SP800_Codes():
    return get_NYSE_Codes(filename="SP800-Oct25.csv")


def get_SP500_Codes():
    return get_NYSE_Codes(filename="SP500-Oct25.csv")


def get_NYSE_Codes_Merged():
    result=get_SP500_Codes()
    result.extend(get_SP400_Codes() ) 
    result.extend(get_SP600_Codes() ) 
    result.extend(get_SP800_Codes() ) 


    return result


def get_NYSE_Codes(filename="SP500-Oct25.csv"):
    df=pd.read_csv(filename)
    
    sp500= list( df.Symbol ) 
    print(len(sp500))

    nas= get_Nasdaq_Codes()
    result=[]

    for s in sp500:
        if (s in nas) or len(s)>=6 :
            #print("appending ", s)
            #result.append(s)
            pass
        else:
            result.append(s)

    print("sp500 count=",len(result))
    return result


def get_Nasdaq_Codes():
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
    codes=get_Nasdaq_Codes()
    count=0
    printTimeStr()

    for c in codes:
        code="TSLA"
        rsi= get_RSI_Single(symbol=c,screener='america',exchange="NASDAQ") 
        print(c, "RSI=",rsi)
        
        count+=1
        if count>=10:
            break

    printTimeStr()

def getCode(key):
    colindex=key.find(":")+1
    return key[colindex:]    


def Go(incNASDAQ=True, incNYSE=True ):

    mydict=[]
    if incNASDAQ and incNYSE:
        dict1=get_multiple_NASDAQ()
        dict2=get_multiple_NYSE()
        merged_dict = {**dict1, **dict2} 
        mydict=merged_dict

    elif incNASDAQ:
        mydict=get_multiple_NASDAQ()
    
    elif incNYSE:
        mydict=get_multiple_NYSE()
    else:
        print("specify atleat one of Nasday NYSE")
        return
    
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

    df=pd.DataFrame( {"Symbol":code_list, "RSI":val_list }) 
    df_sorted = df.sort_values(by=['RSI', 'Symbol'], ascending=[False, True])
    #print(df_sorted.head() )
    return df_sorted



#------------------------------

#print( get_SP500_Codes() )


dfGo=Go(incNASDAQ=True, incNYSE=True)

print("results, head 20")
print( dfGo.head(20) )
resultcodes=dfGo['Symbol']

count,maxcount=0,24
strlist=","
for r in resultcodes:
    strlist= strlist +r +","
    count+=1
    if count==maxcount:
        break

print("\n\n",strlist)





#get_All()


#code="CD"
#rsi= get_RSI_Single(symbol=code,screener='america',exchange="NASDAQ") 
#print(rsi)










print("\n\nhello Mariano Rico. Started the course Sept 28, 2023")
