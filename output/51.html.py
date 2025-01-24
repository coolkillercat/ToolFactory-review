import requests
                
def vat_validation(vat_number):
    api_url = f"https://api.vatcomply.com/vat?vat_number=NL810462783B01"
    querystring = {'vat_number': vat_number, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
vat_validation('NL810462783B01')

import requests
                
def latest_rates():
    api_url = f"https://api.vatcomply.com/rates"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
latest_rates()

import requests
                
def base_rate():
    api_url = f"https://api.vatcomply.com/rates?base=USD"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
base_rate()

import requests
                
def historical_rates():
    api_url = f"https://api.vatcomply.com/rates?date=2000-04-05"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
historical_rates()

import requests
                
def currencies():
    api_url = f"https://api.vatcomply.com/currencies"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
currencies()

import requests
                
def geolocation():
    api_url = f"https://api.vatcomply.com/geolocate"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
geolocation()

