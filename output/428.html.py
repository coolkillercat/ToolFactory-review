import requests
                
def latest_rates():
    api_url = f"/latest"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
latest_rates()

import requests
                
def historical_rates(date):
    api_url = f"/{date}"
    querystring = {'date': date, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
historical_rates('1999-01-04')

import requests
                
def time_series(start_date):
    api_url = f"/{start_date}..{end_date}"
    querystring = {'start_date': start_date, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
time_series('2020-01-01')

import requests
                
def convert_currency(amount, from, to):
    api_url = f"/latest"
    querystring = {'amount': amount, 'from': from, 'to': to, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
convert_currency(10, 'GBP', 'USD')

import requests
                
def list_currencies():
    api_url = f"/currencies"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_currencies()

