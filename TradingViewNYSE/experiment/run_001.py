from datetime import datetime

#import pandas as pd
#import pandas_ta as ta


#df = pd.DataFrame().ta.ticker("aapl")
#rsi =ta.rsi
#print( help(ta) )


print("ready pandas")

def do_stringsave(txtfilename, string_tosave):
    dir="C:\\Users\\USER\\Downloads\\Udemy2023\\DJango\\course001\\Udemy-VSC-Django001\\tradingViewNYSE\\txtfiles\\"

    with open( (dir+txtfilename), 'w') as file:    
        file.write(string_tosave)

    print("finished saving to:",txtfilename) 
    return 1



def getDatedTextFile(prefix):
    # Get the current month
    m = datetime.now().month
    d = datetime.now().day

    strmonth=str(m)
    strday=str(d)
    if d<10:
        strday="0"+str(d)
    
    result= prefix+strmonth+"-"+strday+".txt"
    print(result)
    return result
    


file=getDatedTextFile("testsave")
somestring ="hello\nsaving\nthis\nstring\nbye\n002\n"

do_stringsave(file,somestring)


