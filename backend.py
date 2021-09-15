from urllib.request import urlopen
import requests
import json, csv, os, test
from os import name, path
import yfinance as yf
from fuzzywuzzy import process
import datetime

def filecheck(f):
    if path.exists("./data/"+f)==False:
        with open(os.path.join("./data", f), 'w') as fp:
            print("File created: "+f)
            pass
    else:
        print("File already exist: "+f)
    
def getCompany(text):
    r = requests.get('https://api.iextrading.com/1.0/ref-data/symbols')
    stockList = r.json()
    return process.extractOne(text, stockList)[0]

""" ---------------------------------------------------Stock Details------------------------------------------------------------------"""

def daily_o_c(name, date):
    url = test.daily_o_c_api(name,date)
    # remove above line and add
    # url = "https://api.polygon.io/v1/open-close/"+name+"/"+ str(date)+"?adjusted=true&apiKey=<YOUR_API_KEY>"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

""" ----------------------------------------------------------------------------------------------------------------------------------"""



def groupedBars(date):
    url = test.groupedBars_api(str(datetime.datetime.now().date()))
    # remove above line and add
    # url = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/"+date+"?adjusted=true&apiKey=<YOUR_API_KEY>"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

def refresh():
    filecheck("stock.csv")
    fields = ["symbol", "name"]
    data = []
    data_bars = groupedBars(str(datetime.datetime.today()))
    for value in data_bars["results"]:
        symbol = value["T"]
        company_name = getCompany(symbol.upper())['name']
        data.append([symbol,company_name])
    filepath = "./data/stock.csv"
    with open(filepath, 'w') as csvfile:
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields) 
        csvwriter.writerows(data)
refresh()


