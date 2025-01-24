import requests
                
def crypto_spot_exchange_api(uuid, event, channel, symbol, exchange, duration, refundInvoice):
    api_url = f"missing"
    querystring = {'uuid': uuid, 'event': event, 'channel': channel, 'symbol': symbol, 'exchange': exchange, 'duration': duration, 'refundInvoice': refundInvoice, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
crypto_spot_exchange_api('123e4567-e89b-12d3-a456-426655440000', 'subscribe', 'tickers', 'BTCUSDT', 'binance', 15000, 'lnbcrt1pdace6qpp5my6nc58d50r5gk38ynyz...')

import requests
                
def crypto_futures_exchange_api(uuid, event, channel, symbol, exchange, duration, refundInvoice, interval):
    api_url = f"missing"
    querystring = {'uuid': uuid, 'event': event, 'channel': channel, 'symbol': symbol, 'exchange': exchange, 'duration': duration, 'refundInvoice': refundInvoice, 'interval': 'perpetual', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
crypto_futures_exchange_api('123e4567-e89b-12d3-a456-426655440000', 'subscribe', 'tickers', 'BTCUSD', 'kraken', 15000, 'lnbcrt1pdace6qpp5my6nc58d50r5gk38ynyz...', 'quarterly')

import requests
                
def historical_prices_data_api(exchange, pair, period, year):
    api_url = f"https://api.suredbits.com/historical/v0"
    querystring = {'exchange': exchange, 'pair': pair, 'period': period, 'year': year, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
historical_prices_data_api('bitstamp', 'BTCUSD', 'daily', 2018)

import requests
                
def nfl_data_api(uuid, channel, lastName, firstName):
    api_url = f"https://api.suredbits.com/nfl/v0"
    querystring = {'uuid': uuid, 'channel': channel, 'lastName': lastName, 'firstName': firstName, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
nfl_data_api('123e4567-e89b-12d3-a456-426655440000', 'players', 'Brady', 'Tom')

import requests
                
def nba_data_api(uuid, channel, lastName, firstName):
    api_url = f"https://api.suredbits.com/nba/v0"
    querystring = {'uuid': uuid, 'channel': channel, 'lastName': lastName, 'firstName': firstName, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
nba_data_api('123e4567-e89b-12d3-a456-426655440000', 'players', 'James', 'Lebron')

