from urllib.request import urlopen
import json

def daily_o_c(name, date):
    url = "https://api.polygon.io/v1/open-close/"+name+"/"+ str(date)+"?adjusted=true&apiKey=llQvmrJ_Cr2t5iPAii02EgeiD2hY8Fr2"
    # url = "https://api.polygon.io/v1/open-close/AAPL/2020-10-14?adjusted=true&apiKey=llQvmrJ_Cr2t5iPAii02EgeiD2hY8Fr2"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

