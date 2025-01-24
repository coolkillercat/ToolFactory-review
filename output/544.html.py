import requests
                
def get_current_exchange_rate(base, symbols):
    api_url = f"missing"
    querystring = {'base': base, 'symbols': symbols, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_current_exchange_rate('USD', 'EUR')

import requests
                
def get_historical_exchange_rate(base, symbols, date):
    api_url = f"missing"
    querystring = {'base': base, 'symbols': symbols, 'date': date, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_historical_exchange_rate('USD', 'EUR', '2023-01-01')

import requests
                
def convert_currency(from, to, amount):
    api_url = f"missing"
    querystring = {'from': from, 'to': to, 'amount': amount, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
convert_currency('USD', 'EUR', 100)

import requests
                
def get_time_series_data(base, symbols, start_date, end_date):
    api_url = f"missing"
    querystring = {'base': base, 'symbols': symbols, 'start_date': start_date, 'end_date': end_date, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_time_series_data('USD', 'EUR', '2023-01-01', '2023-01-31')

