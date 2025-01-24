import requests
                
def get_supported_currency_pairs():
    api_url = f"https://www.freeforexapi.com/api/live"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_supported_currency_pairs()

import requests
                
def get_rates_data(pairs):
    api_url = f"https://www.freeforexapi.com/api/live"
    querystring = {'pairs': pairs, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_rates_data('EURUSD,USDJPY')

