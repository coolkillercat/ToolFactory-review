import requests
                
def get_key_value(key):
    api_url = f"https://api.countapi.xyz/get/:namespace?/:key"
    querystring = {'key': key, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_key_value('test')

import requests
                
def set_key_value(key, value):
    api_url = f"https://api.countapi.xyz/set/:namespace?/:key?value=:value"
    querystring = {'key': key, 'value': value, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
set_key_value('test', 69)

import requests
                
def update_key_value(key, amount):
    api_url = f"https://api.countapi.xyz/update/:namespace?/:key?amount=:amount"
    querystring = {'key': key, 'amount': amount, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
update_key_value('test', 5)

import requests
                
def hit_key(key):
    api_url = f"https://api.countapi.xyz/hit/:namespace?/:key"
    querystring = {'key': key, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
hit_key('visits')

import requests
                
def create_key():
    api_url = f"https://api.countapi.xyz/create"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_key()

import requests
                
def get_key_info(key):
    api_url = f"https://api.countapi.xyz/info/:namespace?/:key"
    querystring = {'key': key, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_key_info('test')

import requests
                
def get_api_stats():
    api_url = f"https://api.countapi.xyz/stats"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_api_stats()

