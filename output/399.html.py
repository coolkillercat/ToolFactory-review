import requests
                
def get_item_details(itemId):
    api_url = f"missing"
    querystring = {'itemId': itemId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_item_details(12345)

import requests
                
def get_item_listings(itemId):
    api_url = f"missing"
    querystring = {'itemId': itemId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_item_listings(12345)

import requests
                
def get_item_prices(itemId):
    api_url = f"missing"
    querystring = {'itemId': itemId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_item_prices(12345)

