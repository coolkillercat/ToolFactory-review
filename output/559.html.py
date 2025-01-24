import requests
                
def grab_a_random_joke():
    api_url = f"https://official-joke-api.appspot.com/random_joke"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
grab_a_random_joke()

import requests
                
def grab_ten_random_jokes():
    api_url = f"https://official-joke-api.appspot.com/random_ten"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
grab_ten_random_jokes()

import requests
                
def grab_jokes_by_type__random_(type):
    api_url = f"https://official-joke-api.appspot.com/jokes/:type/random"
    querystring = {'type': type, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
grab_jokes_by_type__random_('programming')

import requests
                
def grab_jokes_by_type__ten_(type):
    api_url = f"https://official-joke-api.appspot.com/jokes/:type/ten"
    querystring = {'type': type, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
grab_jokes_by_type__ten_('programming')

import requests
                
def grab_joke_by_id(id):
    api_url = f"https://official-joke-api.appspot.com/jokes/:id"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
grab_joke_by_id('123')

