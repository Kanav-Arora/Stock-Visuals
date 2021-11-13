def daily_o_c_api(name,date):
    url = "https://api.polygon.io/v1/open-close/"+name+"/"+ str(date)+"?adjusted=true&apiKey=llQvmrJ_Cr2t5iPAii02EgeiD2hY8Fr2"
    return url


def groupedBars_api(date):
    url = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/"+str(date)+"?adjusted=true&apiKey=llQvmrJ_Cr2t5iPAii02EgeiD2hY8Fr2"
    return url

def crypto_daily_o_c_api(name,date):
    url = "https://api.polygon.io/v1/open-close/crypto/"+ name +"/USD/"+  str(date) + "?adjusted=true&apiKey=llQvmrJ_Cr2t5iPAii02EgeiD2hY8Fr2"
    return url

def stocks_aggregate_api(from_date, to_date, ticker):
    url = "https://api.polygon.io/v2/aggs/ticker/"+ ticker +"/range/1/day/"+ from_date+"/"+to_date+"?adjusted=true&sort=asc&limit=120&apiKey=llQvmrJ_Cr2t5iPAii02EgeiD2hY8Fr2"
    return url