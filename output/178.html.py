import requests
                
def get_symbols():
    api_url = f"https://api.gemini.com/v1/symbols"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_symbols()

import requests
                
def get_symbol_details(symbol):
    api_url = f"https://api.gemini.com/v1/symbols/details/:symbol"
    querystring = {'symbol': symbol, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_symbol_details('BTCUSD')

import requests
                
def get_ticker(symbol):
    api_url = f"https://api.gemini.com/v1/pubticker/:symbol"
    querystring = {'symbol': symbol, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_ticker('BTCUSD')

import requests
                
def get_order_book(symbol):
    api_url = f"https://api.gemini.com/v1/book/:symbol"
    querystring = {'symbol': symbol, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_order_book('BTCUSD')

import requests
                
def get_trade_history(symbol):
    api_url = f"https://api.gemini.com/v1/trades/:symbol"
    querystring = {'symbol': symbol, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_trade_history('BTCUSD')

import requests
                
def new_order(request, nonce, symbol, amount, price, side, type):
    api_url = f"https://api.gemini.com/v1/order/new"
    payload = {'request': request, 'nonce': nonce, 'symbol': symbol, 'amount': amount, 'price': price, 'side': side, 'type': type, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
new_order('/v1/order/new', 123456, 'btcusd', '5', '3633.00', 'buy', 'exchange limit')

import requests
                
def cancel_order(request, nonce, order_id):
    api_url = f"https://api.gemini.com/v1/order/cancel"
    payload = {'request': request, 'nonce': nonce, 'order_id': order_id, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
cancel_order('/v1/order/cancel', 123456, 106817811)

import requests
                
def get_order_status(request, nonce, order_id):
    api_url = f"https://api.gemini.com/v1/order/status"
    payload = {'request': request, 'nonce': nonce, 'order_id': order_id, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_order_status('/v1/order/status', 123456, 123456789012345)

import requests
                
def get_active_orders(request, nonce):
    api_url = f"https://api.gemini.com/v1/orders"
    payload = {'request': request, 'nonce': nonce, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_active_orders('/v1/orders', 123456)

import requests
                
def get_past_trades(request, nonce):
    api_url = f"https://api.gemini.com/v1/mytrades"
    payload = {'request': request, 'nonce': nonce, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_past_trades('/v1/mytrades', 123456)

import requests
                
def get_available_balances(request, nonce):
    api_url = f"https://api.gemini.com/v1/balances"
    payload = {'request': request, 'nonce': nonce, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_available_balances('/v1/balances', 123456)

import requests
                
def get_notional_balances(request, nonce):
    api_url = f"https://api.gemini.com/v1/notionalbalances/:currency"
    payload = {'request': request, 'nonce': nonce, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_notional_balances('/v1/notionalbalances/usd', 123456)

