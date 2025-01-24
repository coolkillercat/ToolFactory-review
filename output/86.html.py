import requests
                
def get_global_data():
    api_url = f"https://covid19api.azurewebsites.net/global"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_global_data()

import requests
                
def get_country_data(country):
    api_url = f"https://covid19api.azurewebsites.net/country"
    querystring = {'country': country, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_country_data('USA')

import requests
                
def get_timeseries_data():
    api_url = f"https://covid19api.azurewebsites.net/timeseries"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_timeseries_data()

