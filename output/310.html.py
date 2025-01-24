import requests
                
def current_table_of_exchange_rates(table):
    api_url = f"http://api.nbp.pl/api/exchangerates/tables/{table}/"
    querystring = {'table': table, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
current_table_of_exchange_rates('A')

import requests
                
def series_of_latest_tables_of_exchange_rates(table, topCount):
    api_url = f"http://api.nbp.pl/api/exchangerates/tables/{table}/last/{topCount}/"
    querystring = {'table': table, 'topCount': topCount, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
series_of_latest_tables_of_exchange_rates('A', 10)

import requests
                
def exchange_rate_table_published_today(table):
    api_url = f"http://api.nbp.pl/api/exchangerates/tables/{table}/today/"
    querystring = {'table': table, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
exchange_rate_table_published_today('A')

import requests
                
def exchange_rate_table_published_on_specific_date(table, date):
    api_url = f"http://api.nbp.pl/api/exchangerates/tables/{table}/{date}/"
    querystring = {'table': table, 'date': date, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
exchange_rate_table_published_on_specific_date('A', '2022-01-01')

import requests
                
def series_of_exchange_rate_tables_published_in_date_range(table, startDate, endDate):
    api_url = f"http://api.nbp.pl/api/exchangerates/tables/{table}/{startDate}/{endDate}/"
    querystring = {'table': table, 'startDate': startDate, 'endDate': endDate, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
series_of_exchange_rate_tables_published_in_date_range('A', '2022-01-01', '2022-01-31')

import requests
                
def current_exchange_rate_of_a_currency(table, code):
    api_url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/"
    querystring = {'table': table, 'code': code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
current_exchange_rate_of_a_currency('A', 'USD')

import requests
                
def series_of_latest_exchange_rates_of_a_currency(table, code, topCount):
    api_url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/last/{topCount}/"
    querystring = {'table': table, 'code': code, 'topCount': topCount, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
series_of_latest_exchange_rates_of_a_currency('A', 'USD', 10)

import requests
                
def exchange_rate_of_a_currency_published_today(table, code):
    api_url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/"
    querystring = {'table': table, 'code': code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
exchange_rate_of_a_currency_published_today('A', 'USD')

import requests
                
def exchange_rate_of_a_currency_published_on_specific_date(table, code, date):
    api_url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{date}/"
    querystring = {'table': table, 'code': code, 'date': date, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
exchange_rate_of_a_currency_published_on_specific_date('A', 'USD', '2022-01-01')

import requests
                
def series_of_exchange_rates_of_a_currency_published_in_date_range(table, code, startDate, endDate):
    api_url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{startDate}/{endDate}/"
    querystring = {'table': table, 'code': code, 'startDate': startDate, 'endDate': endDate, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
series_of_exchange_rates_of_a_currency_published_in_date_range('A', 'USD', '2022-01-01', '2022-01-31')

import requests
                
def current_gold_price():
    api_url = f"http://api.nbp.pl/api/cenyzlota/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
current_gold_price()

import requests
                
def series_of_latest_gold_prices(topCount):
    api_url = f"http://api.nbp.pl/api/cenyzlota/last/{topCount}/"
    querystring = {'topCount': topCount, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
series_of_latest_gold_prices(10)

import requests
                
def gold_price_published_today():
    api_url = f"http://api.nbp.pl/api/cenyzlota/today/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
gold_price_published_today()

import requests
                
def gold_price_published_on_specific_date(date):
    api_url = f"http://api.nbp.pl/api/cenyzlota/{date}/"
    querystring = {'date': date, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
gold_price_published_on_specific_date('2022-01-01')

import requests
                
def series_of_gold_prices_published_in_date_range(startDate, endDate):
    api_url = f"http://api.nbp.pl/api/cenyzlota/{startDate}/{endDate}/"
    querystring = {'startDate': startDate, 'endDate': endDate, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
series_of_gold_prices_published_in_date_range('2022-01-01', '2022-01-31')

