

from tradingview_ta import TA_Handler, Interval, Exchange
import pandas as pd
import datetime

from tradingview_ta import *

global_dict_codes={}


##  -------------  Etrade ------------------------------
def get_Multiple_Analysis_Etrade():

    codes=get_Etrade_Codes2()
    return get_Multiple_GENERIC(screener="australia",exchange="ASX",codes=codes)
    #return get_Multiple_GENERIC(screener="america",exchange="nasdaq",codes=codes)



def get_Etrade_Codes2():
    df = pd.read_csv("listcorpOct26.csv")
    result1= list( df['Symbol'] )
    result2=[]

    for r in result1:
        if type(r)==str and len(r)>=3:
            result2.append(r)

    #result=['MIN','WHC','WOR','BHP']
    #print("type etradeCodes=",type(result))
    updateDictionary(result2,'2000')
    return result2
# --------------------------------------------------------

def get_Etrade_Codes1_NOTNEEDED():
    result=['MIN','WHC','WOR','BHP','VSL']
    #result=['AAPL','MSFT','IBM','TSLA']

    updateDictionary(result,'2000')
    return result


def get_Etrade_Individually_NOTNEEDED(maxcount=20):
    printTimeStr()
    codes=get_Etrade_Codes1()
    count=0

    for c in codes:
        print("getting",c)
        #rec=get_Summary_Single(symbol=c, screener='australia',exchange="ASX")
        
        rec = fetchAnalysis_Single(c,'australia','ASX').summary 
        #print(type(rec))
        val= rec['BUY']-rec['SELL']
        
        star=""
        if val>15:
            star="**"
        
        count+=1
        print(count,c,">>",rec, star) 
        
        if count==maxcount:
            break

    printTimeStr()
    pass


##  -----------------------------------------------------------------------




def get_multiple_NYSE():
    codes=get_NYSE_Codes_Merged()
    
    return get_Multiple_GENERIC(screener="america",exchange="NYSE",codes=codes)


def get_multiple_NASDAQ():
    codes=get_Nasdaq_Codes()
    return get_Multiple_GENERIC(screener="america",exchange="nasdaq",codes=codes)

def get_Multiple_GENERIC(screener="america",exchange="nasdaq", codes=['TSLA',"AAPL"]):

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

    analysis = get_multiple_analysis(screener=screener, interval=Interval.INTERVAL_1_MINUTE,symbols=naslist)
    

        #symbols=["nasdaq:AAL", "nasdaq:AAOI", "nasdaq:AAON", "nasdaq:AAPL", "nasdaq:ABCB",\
        #        "nasdaq:ABCL", "nasdaq:ABCM", "nasdaq:ABNB", "nasdaq:ACAD", "nasdaq:ACAH"])

    printTimeStr()

    #print("type analysis=",type(analysis))
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

def get_Summary_Single(symbol="TSLA", screener='america',exchange="NASDAQ"):
    summary = fetchAnalysis_Single(symbol,screener,exchange).summary 
    #print(symbol+" Summary\n",summary)
    return symbol+" >>  "+ str(summary)





def get_SP400_Codes():
    result= get_NYSE_Codes(filename="SP400-Oct25.csv")
    updateDictionary(result,'400')
    return result

def get_SP600_Codes():
    result= get_NYSE_Codes(filename="SP600-Oct25.csv")
    updateDictionary(result,'600')
    return result

def get_SP800_Codes():
    result= get_NYSE_Codes(filename="SP800-Oct25.csv")
    updateDictionary(result,'800')
    return result
    
def get_SP8002_Codes():    
    result= get_NYSE_Codes(filename="SP8002-Oct25.csv")
    updateDictionary(result,'800')
    return result


def get_SP500_Codes():
    result= get_NYSE_Codes(filename="SP500-Oct25.csv")
    updateDictionary(result,'500')
    return result

def updateDictionary(codelist=[], market='500'):
    global global_dict_codes
    
    for c in codelist:
        if global_dict_codes.get(c)==None: 
            global_dict_codes[c]=market
        pass
    pass



def get_NYSE_Codes_Merged():
    result=get_SP500_Codes()
    result.extend(get_SP400_Codes() ) 
    result.extend(get_SP600_Codes() ) 
    result.extend(get_SP800_Codes() ) 
    result.extend(get_SP8002_Codes() ) 



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
    updateDictionary(result,'700')

    return result

def printTimeStr():
    # Get the current date and time
    current_time = datetime.datetime.now()

    # Format the current time as a string
    strTime = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("\n","*** TIME=",strTime,"\n")  


# too slow
def get_All_Individually():
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

def getCleanCode(key):
    colindex=key.find(":")+1
    return key[colindex:]  

def printDictionary(whichMT='500', maxcount=10):
    count=0
    for k in global_dict_codes:
        mt=global_dict_codes[k]
        if mt==whichMT:
            print(k, mt)
            count+=1
        if count==maxcount:
            break
        pass



def Go(incEtrade=False, incNASDAQ=True, incNYSE=True, maxcount=24, savefile="Recommend-Oct25.csv",method=1 ):

    mydict=[]

    if incEtrade:

        print("Etrade 001")
        mydict=get_Multiple_Analysis_Etrade()
        print("Etrade 002")
        #print(mydict)

    elif incNASDAQ and incNYSE:
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
    markets=[]
    #print("mydict type=", type(mydict) )

    count=0
    for k in mydict:
        val=mydict[k]
        if val != None:

            if method==1:  
                val=mydict[k].indicators['RSI']
            elif method==2:
                summary=mydict[k].summary
                val=summary['BUY']-summary['SELL'] 
            else:
                val=0       
            
            code=getCleanCode(k)

            val_list.append(val)
            code_list.append(code)
            markets.append(global_dict_codes.get(code))

            
            #print(count,k,code ,val)
        count+=1

    value_name="Unknown" 
    if method==1:
        value_name="RSI"
    elif method==2:
        value_name="buys"


    df  = pd.DataFrame( {"Symbol":code_list, value_name:val_list, "MT":markets }) 
    df_sorted = df.sort_values(by=[value_name, 'Symbol'], ascending=[False, True]).round(1)
    df_sorted.to_csv(savefile,index=None)


    
    #print("results, head "+str(maxcount) )    
    #print(df_sorted.head(maxcount) )

    resultcodes=list(df_sorted['Symbol'])
    resultrsi=list(df_sorted[value_name])

    size=len(resultcodes)
    if size<maxcount:
        maxcount=size
    
    #print("result---")
    #print(resultcodes)
    
    count=0
    strlist=","
    for i in range(maxcount):
        strlist= strlist +resultcodes[i] +","+str(resultrsi[i])+","
        count+=1
        if count==10:
            strlist+="\n"
            count=0


    #print("\n\n",strlist)
    return strlist, df_sorted



#------------------------------

if __name__ =="__main__":
    #get_Summary_Single(symbol="NUTX", screener='america',exchange="NASDAQ")
    get_Summary_Single(symbol="AVD", screener='america',exchange="NYSE")


    if False:
        Go(incNASDAQ=True, incNYSE=True, maxcount=40, savefile="Recommend-Oct25.csv",method=2)
        printDictionary(whichMT='400', maxcount=10)
        printDictionary(whichMT='500', maxcount=10)
        printDictionary(whichMT='600', maxcount=10)
        printDictionary(whichMT='700', maxcount=10)
        printDictionary(whichMT='800', maxcount=10)


    #get_All_Individually()






#get_All()


#code="CD"
#rsi= get_RSI_Single(symbol=code,screener='america',exchange="NASDAQ") 
#print(rsi)











