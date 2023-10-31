"""
MIT License

Copyright (c) 2023 hunter87

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
import requests as req
from bs4 import BeautifulSoup as bs

def currency_convert(frm:str, to:str, amount:int):
    frm = frm.upper()
    to = to.upper()
    #print(frm, to, amount)
    url = f"https://xe.com/currencyconverter/convert/?Amount={amount}&From={frm}&To={to}"  #you can use your api if you have
    data = req.get(url).text
    soup = bs(data, "html.parser")
    rate = soup.find("p", {"class": "dPdXSB"}).text 
    return rate

matches = [
    {"query": ["usd to inr", " usd to inr", "usd to inr", " usd inr", "usd inr", "usd in inr"], "frm": "usd", "to": "inr"},
    {"query": ["inr to usd", " inr to usd", "inr to usd", " inr usd", "inr usd", "inr in usd"], "frm": "inr", "to": "usd"},
    {"query": ["usd to eur", " usd to eur", "usd to eur", " usd eur", "usd eur", "usd in euro"], "frm": "usd", "to": "eur"},
    {"query": ["eur to usd", " eur to usd", "eur to usd", " eur usd", "eur usd", "euro in usd"], "frm": "eur", "to": "usd"},
    {"query": ["usd to gbp", " usd to gbp", "usd to gbp", " usd gbp", "usd gbp", "usd in gdp"], "frm": "usd", "to": "gbp"},
    {"query": ["gbp to usd", " gbp to usd", "gbp to usd", " gbp usd", "gbp usd", "gdp in usd"], "frm": "gbp", "to": "usd"},
    {"query": ["usd to aud", " usd to aud", "usd to aud", " usd aud", "usd aud", "usd in aud"], "frm": "usd", "to": "aud"},
    {"query": ["aud to usd", " aud to usd", "aud to usd", " aud usd", "aud usd", "aud in usd"], "frm": "aud", "to": "usd"},
    {"query": ["usd to cad", " usd to cad", "usd to cad", " usd cad", "usd cad", "usd in cad"], "frm": "usd", "to": "cad"},
    {"query": ["cad to usd", " cad to usd", "cad to usd", " cad usd", "cad usd", "cad in usd"], "frm": "cad", "to": "usd"},
    {"query": ["usd to chf", " usd to chf", "usd to chf", " usd chf", "usd chf", "usd in chf"], "frm": "usd", "to": "chf"},
    {"query": ["usd to pkr", " usd to pkr", "usd to pkr", " usd pkr", "usd pkr", "usd in pkr"], "frm": "usd", "to": "pkr"},
    {"query": ["pkr to usd", " pkr to usd", "pkr to usd", " pkr usd", "pkr usd", "pkr in usd"], "frm": "pkr", "to": "usd"},
    {"query": ["usd to jpy", " usd to jpy", "usd to jpy", " usd jpy", "usd jpy", "usd in jpy"], "frm": "usd", "to": "jpy"},
    {"query": ["jpy to usd", " jpy to usd", "jpy to usd", " jpy usd", "jpy usd", "jpy in usd"], "frm": "jpy", "to": "usd"},
    {"query": ["usd to cny", " usd to cny", "usd to cny", " usd cny", "usd cny", "usd in cny"], "frm": "usd", "to": "cny"},
    {"query": ["cny to usd", " cny to usd", "cny to usd", " cny usd", "cny usd", "cny in usd"], "frm": "cny", "to": "usd"},
    {"query": ["usd to hkd", " usd to hkd", "usd to hkd", " usd hkd", "usd hkd", "usd in hkd"], "frm": "usd", "to": "hkd"},
    {"query": ["hkd to usd", " hkd to usd", "hkd to usd", " hkd usd", "hkd usd", "hkd in usd"], "frm": "hkd", "to": "usd"},
    {"query": ["usd to sgd", " usd to sgd", "usd to sgd", " usd sgd", "usd sgd", "usd in sgd"], "frm": "usd", "to": "sgd"},
    {"query": ["sgd to usd", " sgd to usd", "sgd to usd", " sgd usd", "sgd usd", "sgd in usd"], "frm": "sgd", "to": "usd"},
    {"query": ["usd to nzd", " usd to nzd", "usd to nzd", " usd nzd", "usd nzd", "usd in nzd"], "frm": "usd", "to": "nzd"},
    {"query": ["nzd to usd", " nzd to usd", "nzd to usd", " nzd usd", "nzd usd", "nzd in usd"], "frm": "nzd", "to": "usd"},
    {"query": ["usd to krw", " usd to krw", "usd to krw", " usd krw", "usd krw", "usd in krw"], "frm": "usd", "to": "krw"},
    {"query": ["krw to usd", " krw to usd", "krw to usd", " krw usd", "krw usd", "krw in usd"], "frm": "krw", "to": "usd"},
    {"query": ["usd to thb", " usd to thb", "usd to thb", " usd thb", "usd thb", "usd in thb"], "frm": "usd", "to": "thb"},
    {"query": ["thb to usd", " thb to usd", "thb to usd", " thb usd", "thb usd", "thb in usd"], "frm": "thb", "to": "usd"},
]

def filter_text(text):
    amt = [x for x in text.split() if x.isdigit()==True]
    if len(amt) == 0:amt = 1
    else:amt = int(amt[0])
    #print(amt)
    for i in matches:
        for j in i["query"]:
            if j in text.lower():
                return currency_convert(i["frm"], i["to"], amt)
    return

#filter_text("convert 5 usd to euro")
