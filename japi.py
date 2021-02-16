import json
import urllib.request

def getStockData(symbol):
    alphaURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+symbol+'&apikey=9DXN4U5GRLZY1X5B'
    connection = urllib.request.urlopen(alphaURL)
    responseString = connection.read().decode()
    return responseString

def main():    
    symbol = None
    while symbol != 'quit':
        symbol = input('Enter a stock symbol: ')
        if symbol == 'quit':
            break
        else:
            getJs=getStockData(symbol)
            jsDict = json.loads(getJs)
            print(getJs)
            stockSymbol = (jsDict["Global Quote"].get("01. symbol"))
            stockPrice = (jsDict["Global Quote"].get("05. price"))
            print("The current price of %s is: $%s\n" % (stockSymbol, stockPrice))
            print("Stock Quotes retrieved successfully!")
main()
