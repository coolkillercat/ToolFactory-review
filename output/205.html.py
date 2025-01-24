import requests
                
def serial_number_search(serialnumber, username, password):
    api_url = f"https://markerapi.com/api/v2/trademarks/serialnumber/{serialnumber}/username/{username}/password/{password}"
    querystring = {'serialnumber': serialnumber, 'username': username, 'password': password, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
serial_number_search('12345678', 'apiuser', 'apipassword')

import requests
                
def trademark_search(search, status, start, username, password):
    api_url = f"https://markerapi.com/api/v2/trademarks/trademark/{search}/status/{status}/start/{start}/username/{username}/password/{password}"
    querystring = {'search': search, 'status': status, 'start': 1, 'username': username, 'password': password, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
trademark_search('starbucks', 'active', 1, 'apiuser', 'apipassword')

import requests
                
def description_search(search, status, start, username, password):
    api_url = f"https://markerapi.com/api/v2/trademarks/description/{search}/status/{status}/start/{start}/username/{username}/password/{password}"
    querystring = {'search': search, 'status': status, 'start': 1, 'username': username, 'password': password, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
description_search('coffee', 'active', 1, 'apiuser', 'apipassword')

import requests
                
def owner_search(owner, status, start, username, password):
    api_url = f"https://markerapi.com/api/v2/trademarks/owner/{owner}/status/{status}/start/{start}/username/{username}/password/{password}"
    querystring = {'owner': owner, 'status': status, 'start': 1, 'username': username, 'password': password, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
owner_search('John Doe', 'active', 1, 'apiuser', 'apipassword')

import requests
                
def expiration_search(timeframe, status, start, username, password):
    api_url = f"https://markerapi.com/api/v2/trademarks/expiration/{timeframe}/status/{status}/start/{start}/username/{username}/password/{password}"
    querystring = {'timeframe': timeframe, 'status': status, 'start': 1, 'username': username, 'password': password, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
expiration_search('6 months', 'active', 1, 'apiuser', 'apipassword')

