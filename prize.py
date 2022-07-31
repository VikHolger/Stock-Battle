import requests
from bs4 import BeautifulSoup
from datetime import datetime

from sklearn import exceptions

stocks = []

#Get stock info
def stock_price(symbol: str) -> str:
    inf = []
    url = f"https://finance.yahoo.com/quote/{symbol}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    #prise
    prz = soup.find("fin-streamer", class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").text.replace(",","")
    inf.append(round((float(prz)), 2))
    #change %
    change = soup.find("fin-streamer", class_="Fw(500) Pstart(8px) Fz(24px)").text
    inf.append(round((float(prz)/(float(prz)-float(change)) - 1) * 100, 2))
    #previous closed
    prz = soup.find("td", class_="Ta(end) Fw(600) Lh(14px)").text
    inf.append(round((float(prz)), 2))
    return inf

#Get the stocks "name"
with open("stocks.stk", "r") as stockFile:
    for stk in stockFile:
        a = stk.split("|")        
        stocks.append(a[0].rstrip())

#stats
n = 0
t = len(stocks)
loading = 0
normal = 0
exeptions = 0
#open stock and get info
for stk in stocks:
    now = datetime.now() #Get the time
    current_time = now.strftime("%m/%d %H:%M:%S")

    #Visual
    if loading == 0:
        print(f"{n}/{t} | .    \n", end="\r")
        loading = 1

    elif loading == 1:
        print(f"{n}/{t} | ..   \n", end="\r")
        loading = 2

    elif loading == 2:
        print(f"{n}/{t} | ... \n", end="\r")
        loading = 0

    try:
        #Get the data/Info aout stock
        inf = stock_price(str(stk))
        line = str(current_time)

        for i in inf:
            line += "|" + str(i) #Saves it to a string
        line += "\n"

        #saves data to file
        with open("./prize/" +str(stk) + ".stk", "a") as f:
            f.write(line)

        normal += 1
    #If it didnt succeed
    except:
        with open("./log/PRZ.log", "a") as log:
            err = str(current_time) + " | err -> could not find URL/Info for stock " + str(stk) + "\n"
            print(err)
            log.write(err)
            exeptions += 1

    n += 1

#Write to Log
now = datetime.now() #Get the time
current_time = now.strftime("%m/%d %H:%M:%S")
with open("./log/PRZ.log", "a") as log:
    info = str(current_time) + " | info -> Uppdated " + str(normal) + " number of stocks, " + str(exeptions) + " exceptions\n"
    print(info)
    log.write(info)