import requests
                
def get_feed_info(feedId):
    api_url = f"https://transit.land/api/v1/feeds/feedId"
    querystring = {'feedId': feedId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_feed_info('123')

import requests
                
def list_feeds():
    api_url = f"https://transit.land/api/v1/feeds"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_feeds()

import requests
                
def get_operator_info(operatorId):
    api_url = f"https://transit.land/api/v1/operators/operatorId"
    querystring = {'operatorId': operatorId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_operator_info('456')

import requests
                
def list_operators():
    api_url = f"https://transit.land/api/v1/operators"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_operators()

