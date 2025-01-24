import requests
                
def get_feed(onestop_id):
    api_url = f"https://transit.land/api/v1/feeds/:onestop_id"
    querystring = {'onestop_id': onestop_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_feed('f-9q9-caltrain')

import requests
                
def get_operator(onestop_id):
    api_url = f"https://transit.land/api/v1/operators/:onestop_id"
    querystring = {'onestop_id': onestop_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_operator('o-9q9-caltrain')

import requests
                
def get_stop(onestop_id):
    api_url = f"https://transit.land/api/v1/stops/:onestop_id"
    querystring = {'onestop_id': onestop_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_stop('s-9q9-caltrain')

import requests
                
def get_route(onestop_id):
    api_url = f"https://transit.land/api/v1/routes/:onestop_id"
    querystring = {'onestop_id': onestop_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_route('r-9q9-caltrain')

