import requests
                
def global_crypto_data():
    api_url = f"https://api.coinlore.net/api/global/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
global_crypto_data()

import requests
                
def tickers__all_coins_():
    api_url = f"https://api.coinlore.net/api/tickers/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
tickers__all_coins_()

import requests
                
def ticker__specific_coin_(id):
    api_url = f"https://api.coinlore.net/api/ticker/?id={ID}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
ticker__specific_coin_('90')

import requests
                
def get_markets_for_coin(id):
    api_url = f"https://api.coinlore.net/api/coin/markets/?id={ID}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_markets_for_coin('90')

import requests
                
def all_exchanges():
    api_url = f"https://api.coinlore.net/api/exchanges/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
all_exchanges()

import requests
                
def fetch_exchange_data(id):
    api_url = f"https://api.coinlore.net/api/exchange/?id={ID}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_exchange_data('5')

import requests
                
def social_stats(id):
    api_url = f"https://api.coinlore.net/api/coin/social_stats/?id={ID}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
social_stats('80')

