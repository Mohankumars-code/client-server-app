#!/usr/bin/env python
# coding: utf-8


import requests 
import pandas as pd
import datetime
import socket
now = datetime.datetime.now()
def web_scrapper(stock):
    headers = {
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.nasdaq.com/',
    'referer': 'https://www.nasdaq.com/',
    'accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

    data = requests.get('https://api.nasdaq.com/api/quote/'+stock+'/info?assetclass=stocks', headers=headers).json()
    if (data != None):
        if (data["data"] != None):
            if (data["data"]["primaryData"] != None):
                if (data["data"]["primaryData"]["lastSalePrice"] != None):
                    quote = data["data"]["primaryData"]["lastSalePrice"]
                    time = now.strftime("%d/%m/%Y, %H:%M:%S:%f")
                else:
                    quote = "NULL"
            else:
                quote = "NULL"
        else:
            quote = "NULL"
    else:
        quote = "NULL"

    return quote,time

soc = socket.socket()
host = socket.gethostname()
port = 20000
soc.bind((host, port))
stock = input("Enter the Stock Ticker(Ex AAPL):")
print("Server is running") 
soc.listen()
conn, addr = soc.accept()
print('Connected Address: ',addr)
data = []
date = []

while True:
    quote,time = web_scrapper(stock)
    pac = time+" "+quote
    conn.send(pac.encode())
    data.append(quote)
    date.append(time)
    df = pd.DataFrame({"Time":date,stock:data})
    df.to_csv('Recorded_data.csv',index=False)
    

soc.close()

    