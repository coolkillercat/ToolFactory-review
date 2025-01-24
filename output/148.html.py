import requests
                
def ticker(coin):
    api_url = f"https://www.mercadobitcoin.net/api/{coin}/ticker/"
    querystring = {'coin': coin, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
ticker('BTC')

import requests
                
def orderbook(coin):
    api_url = f"https://www.mercadobitcoin.net/api/{coin}/orderbook/"
    querystring = {'coin': coin, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
orderbook('BTC')

import requests
                
def trades(coin):
    api_url = f"https://www.mercadobitcoin.net/api/{coin}/trades/"
    querystring = {'coin': coin, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
trades('BTC')

import requests
                
def day_summary(coin, year, month, day):
    api_url = f"https://www.mercadobitcoin.net/api/{coin}/day-summary/{year}/{month}/{day}/"
    querystring = {'coin': coin, 'year': year, 'month': month, 'day': day, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
day_summary('BTC', 2013, 6, 20)

