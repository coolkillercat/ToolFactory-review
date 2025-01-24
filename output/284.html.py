import requests
                
def end_of_day_data(access_key, symbols):
    api_url = f"https://api.marketstack.com/v1/eod"
    querystring = {'access_key': access_key, 'symbols': symbols, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
end_of_day_data('YOUR_ACCESS_KEY', 'AAPL,MSFT')

import requests
                
def intraday_data(access_key, symbols):
    api_url = f"https://api.marketstack.com/v1/intraday"
    querystring = {'access_key': access_key, 'symbols': symbols, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
intraday_data('YOUR_ACCESS_KEY', 'AAPL,MSFT')

import requests
                
def splits_data(access_key, symbols):
    api_url = f"https://api.marketstack.com/v1/splits"
    querystring = {'access_key': access_key, 'symbols': symbols, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
splits_data('YOUR_ACCESS_KEY', 'AAPL,MSFT')

import requests
                
def dividends_data(access_key, symbols):
    api_url = f"https://api.marketstack.com/v1/dividends"
    querystring = {'access_key': access_key, 'symbols': symbols, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
dividends_data('YOUR_ACCESS_KEY', 'AAPL,MSFT')

import requests
                
def tickers(access_key):
    api_url = f"https://api.marketstack.com/v1/tickers"
    querystring = {'access_key': access_key, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
tickers('YOUR_ACCESS_KEY')

import requests
                
def market_indices(access_key, symbols):
    api_url = f"https://api.marketstack.com/v1/eod"
    querystring = {'access_key': access_key, 'symbols': symbols, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
market_indices('YOUR_ACCESS_KEY', 'DJI.INDX')

import requests
                
def exchanges(access_key):
    api_url = f"https://api.marketstack.com/v1/exchanges"
    querystring = {'access_key': access_key, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
exchanges('YOUR_ACCESS_KEY')

import requests
                
def currencies(access_key):
    api_url = f"https://api.marketstack.com/v1/currencies"
    querystring = {'access_key': access_key, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
currencies('YOUR_ACCESS_KEY')

import requests
                
def timezones(access_key):
    api_url = f"https://api.marketstack.com/v1/timezones"
    querystring = {'access_key': access_key, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
timezones('YOUR_ACCESS_KEY')

