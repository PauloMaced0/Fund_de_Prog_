# Constantes para indexar os tuplos:
NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
    lst = loadStockFile("nasdaq.csv")
    # Show just first and last tuples:
    print("first:", lst[1])
    print("last:", lst[-1])
    
    print()
    
    print("a) totVol=", totalVolume(lst))

    print()

    print("b) maxVal=", maxValorization(lst))
    
    print()

    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO'])
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    print()

    port = {'NFLX': 100, 'CSCO': 80}
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {}
    
    for item in lst:
        totVol[item[0]] = item[6] 


    return totVol

def maxValorization(lst):
    vMax = {}
    
    for item in lst:
        valorization = (item[5] / item[3]) * 100
        
        date = item[1]

        if not date in vMax:
            vMax[date] = (item[0], valorization)
        else:
            if vMax[date][1] < valorization:
                vMax[date] = (item[0],valorization)

    return vMax

def stocksByDateByName(lst):
    dic = {}
    
    for item in lst:

        date = item[DATE]
        name = item[NAME]
        val = (item[OPEN], item[MAX], item[MIN], item[CLOSE], item[VOLUME])
        if not date in dic:
            dic[date] = {name : val}
        else:
            dic[date][name] = val
    
    return dic

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    
    for company_name, company_stocks in portfolio.items():

        assert company_name in stocks[date]

        val += stocks[date][company_name][3] * company_stocks

    return val

if __name__ == "__main__":
    main()