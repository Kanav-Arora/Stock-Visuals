from urllib.request import urlopen
import json
import test

def daily_o_c(name, date):
    url = test.daily_o_c_api(name,date)
    # remove above line and add
    # url = "https://api.polygon.io/v1/open-close/"+name+"/"+ str(date)+"?adjusted=true&apiKey=<your_api_key>"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

