import requests
                
def list_all_currencies():
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_all_currencies()

import requests
                
def list_all_currencies__minified_():
    api_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_all_currencies__minified_()

import requests
                
def get_currency_list_with_base_currency(currencyCode):
    api_url = f"missing"
    querystring = {'currencyCode': currencyCode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_currency_list_with_base_currency('eur')

import requests
                
def get_currency_list_with_base_currency_on_specific_date(currencyCode, date):
    api_url = f"missing"
    querystring = {'currencyCode': currencyCode, 'date': date, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_currency_list_with_base_currency_on_specific_date('eur', '2024-02-26')

import requests
                
def get_currency_value_between_two_currencies(baseCurrencyCode, targetCurrencyCode):
    api_url = f"missing"
    querystring = {'baseCurrencyCode': baseCurrencyCode, 'targetCurrencyCode': targetCurrencyCode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_currency_value_between_two_currencies('eur', 'jpy')

