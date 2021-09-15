from urllib.request import urlopen
import json, csv, os, test
from os import path

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
    # url = "https://api.polygon.io/v1/open-close/"+name+"/"+ str(date)+"?adjusted=true&apiKey=<your_api_key>"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

""" ----------------------------------------------------------------------------------------------------------------------------------"""

def refresh():
    filecheck("stock.csv")
    

refresh()
