def daily_o_c_api(name,date):
    url = "https://api.polygon.io/v1/open-close/"+name+"/"+ str(date)+"?adjusted=true&apiKey=llQvmrJ_Cr2t5iPAii02EgeiD2hY8Fr2"
    return url


def groupedBars_api(date):
    url = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/"+str(date)+"?adjusted=true&apiKey=llQvmrJ_Cr2t5iPAii02EgeiD2hY8Fr2"
    return url