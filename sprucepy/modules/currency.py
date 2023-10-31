import config
import requests as req
from bs4 import BeautifulSoup as bs

def currency_convert(frm:str, to:str, amount:int):
    frm = frm.upper()
    to = to.upper()
    #print(frm, to, amount)
    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={frm}&To={to}"  #you can use your api if you have
    data = req.get(url).text
    soup = bs(data, "html.parser")
    rate = soup.find("p", {"class": "dPdXSB"}).text  #dPdXSB
    print(rate)


def filter_text(text):
    amt = [x for x in text.split() if x.isdigit()==True]
    if len(amt) == 0:amt = 1
    else:amt = int(amt[0])
    #print(amt)
    for i in matches:
        for j in i["query"]:
            if j in text.lower():
                return currency_convert(i["frm"], i["to"], amt)

#filter_text("convert 5 usd to euro")
