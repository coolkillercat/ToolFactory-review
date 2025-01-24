import requests
                
def hebrew_date_converter_rest_api(gregorianDate):
    api_url = f"missing"
    querystring = {'gregorianDate': gregorianDate, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
hebrew_date_converter_rest_api('2023-10-01')

import requests
                
def jewish_calendar_rest_api():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
jewish_calendar_rest_api()

import requests
                
def leyning__torah_reading__api():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
leyning__torah_reading__api()

import requests
                
def shabbat_times_rest_api(location):
    api_url = f"missing"
    querystring = {'location': location, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
shabbat_times_rest_api('New York, NY')

import requests
                
def yahrzeit___anniversary_api(name, gregorianDate):
    api_url = f"missing"
    querystring = {'name': name, 'gregorianDate': gregorianDate, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
yahrzeit___anniversary_api('John Doe', '2023-10-01')

import requests
                
def zmanim_api(location):
    api_url = f"missing"
    querystring = {'location': location, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
zmanim_api('New York, NY')

