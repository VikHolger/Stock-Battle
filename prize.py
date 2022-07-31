import requests
from bs4 import BeautifulSoup
from datetime import datetime

stocks = []

def stock_price(symbol: str = "AAPL") -> str:
    inf = []
    url = f"https://finance.yahoo.com/quote/{symbol}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    #prise
    prz = soup.find("fin-streamer", class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").text
    inf.append(round((float(prz)), 2))
    #change %
    change = soup.find("fin-streamer", class_="Fw(500) Pstart(8px) Fz(24px)").text
    inf.append(round((float(prz)/(float(prz)-float(change)) - 1) * 100, 2))
    #previous closed
    prz = soup.find("td", class_="Ta(end) Fw(600) Lh(14px)").text
    inf.append(round((float(prz)), 2))
    return inf


with open("stocks.stk", "r") as stockFile:
    for stk in stockFile:
        stocks.append(stk.rstrip("\n"))

for stk in stocks:
    inf = stock_price(stk)
    now = datetime.now()
    current_time = now.strftime("%m/%d %H:%M:%S")
    line = str(current_time)
    for i in inf:
        line += "|" + str(i)

    with open("./prize/" +str(stk) + ".stk", "a") as f:
        f.write(line)