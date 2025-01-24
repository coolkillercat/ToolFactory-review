import requests
                
def get_zip_codes():
    api_url = f"https://sepomex.icalialabs.com/api/v1/zip_codes"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_zip_codes()

import requests
                
def get_states():
    api_url = f"https://sepomex.icalialabs.com/api/v1/states"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_states()

import requests
                
def get_municipalities():
    api_url = f"https://sepomex.icalialabs.com/api/v1/municipalities"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_municipalities()

import requests
                
def get_cities():
    api_url = f"https://sepomex.icalialabs.com/api/v1/cities"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_cities()

