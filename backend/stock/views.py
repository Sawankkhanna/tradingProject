from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from exchange.models import Exchange
from .models import Stock
from .serializers import StockSerializer

maxStock = {
        'maxPercent': -1000,
        'name': 'AAAA'
    }

resultData = []

@api_view(['POST'])
def getAllStocks(request):
    exchange = Exchange()
    exchange.exchangeID = 'NYSEus'
    exchange.exchangeName = 'NYSE'
    exchange.currency = 'USD'
    exchange.country = 'USA'
    url = "https://twelve-data1.p.rapidapi.com/stocks"
    querystring = {"exchange": exchange.exchangeName, "format": "json"}
    headers = {
	    "X-RapidAPI-Key": "c7363c18fbmsh19cafb5d660de9ap103768jsnac4fb27f97dc",
	    "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    count = 0
    stockList = ''
    for stock in response.json()['data']:
        count += 1
        if count<=200:
            stockList = stockList + stock['symbol'] + ','
        else:
            stockList
            callNextAPI(stockList[:-1])
            stockList = stock['symbol'] + ','
            count = 1
    if len(stockList) !=0:
        callNextAPI(stockList[:-1])
    maxStock['resultData'] = resultData
    return Response(maxStock)

def callNextAPI(stockList):
    url = "https://mboum-finance.p.rapidapi.com/qu/quote"
    querystring = {"symbol":stockList}
    headers = {
        "X-RapidAPI-Key": "c7363c18fbmsh19cafb5d660de9ap103768jsnac4fb27f97dc",
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    

    for result in response.json():
        if result['postMarketChangePercent']!=None and result['postMarketChangePercent'] > maxStock['maxPercent']:
            maxStock['maxPercent'] = result['postMarketChangePercent']
            maxStock['name'] = result['symbol']

        data = {
                "symbol": '',
                "name": '',
                "marketCap": 0,
                "exchange": "NYSE",
                "postMarketChangePercent": 0,
                "regularMarketPrice": 0,
                "regularMarketChangePercent": 0
            }
        
        if 'symbol' in result:
            data['symbol'] = result['symbol']
        if 'longName' in result:
            data['name'] = result['longName']
        if 'marketCap' in result:
            data['marketCap'] = result['marketCap']
        if 'postMarketChangePercent' in result:
            data['postMarketChangePercent'] = result['postMarketChangePercent']
        if 'regularMarketPrice' in result:
            if result['regularMarketPrice'] < 1:
                newStockFound = {'symbol': data['symbol'], 'exchange': data['exchange'], 'name': data['name'], 'price': result['regularMarketPrice']}
                resultData.append(newStockFound)
            data['regularMarketPrice'] = result['regularMarketPrice']
        if 'regularMarketChangePercent' in result:
            data['regularMarketChangePercent'] = result['regularMarketChangePercent']
            
        stock = Stock.objects.create(**data)
        serializer = StockSerializer(stock, many=False)