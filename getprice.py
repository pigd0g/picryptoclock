#!/usr/bin/env python3

import json 
import requests 

#Bitcoin Price
r = requests.get('https://api.coinmarketcap.com/v2/ticker/1/')

data = r.json()

price = int(data["data"]["quotes"]["USD"]["price"])

#for coin in r.json():
    #print(coin["price_usd"])

pricestr = str(format(price, ",d"))

#Market Cap    
r = requests.get('https://api.coinmarketcap.com/v2/global/')    
data = r.json()
    
mcap = int(data["data"]["quotes"]["USD"]["total_market_cap"])    
    
mcap = mcap / 1000000000

pricestr = pricestr + "|" + str(mcap)

file = open("/home/pi/picryptoclock/btcprice.txt","w") 
file.write(pricestr)
file.close()

