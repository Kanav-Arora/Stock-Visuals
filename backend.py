from urllib.request import urlopen
import requests
import json, csv, os, test
from os import name, path
import datetime

def filecheck(f):
    if path.exists("./data/"+f)==False:
        with open(os.path.join("./data", f), 'w') as fp:
            print("File created: "+f)
            pass
    else:
        print("File already exist: "+f)
    

""" ---------------------------------------------------Stock Details------------------------------------------------------------------"""

def daily_o_c(name, date):
    url = test.daily_o_c_api(name,date)
    # remove above line and add
    # url = "https://api.polygon.io/v1/open-close/"+name+"/"+ str(date)+"?adjusted=true&apiKey=<YOUR_API_KEY>"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

""" ----------------------------------------------------------------------------------------------------------------------------------"""


""" ---------------------------------------------------Stock Listing------------------------------------------------------------------"""
def refresh():
    filecheck("stock.csv")
    file = open("./data/stock.csv")
    csvread = csv.reader(file)
    data = []
    for row in csvread:
        data.append(row)
    return data


""" ----------------------------------------------------------------------------------------------------------------------------------"""


