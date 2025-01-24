import requests
                
def sources():
    api_url = f"https://www.econdb.com/api/sources/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
sources()

import requests
                
def datasets():
    api_url = f"https://www.econdb.com/api/datasets/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
datasets()

import requests
                
def series():
    api_url = f"https://www.econdb.com/api/series/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
series()

import requests
                
def companies():
    api_url = f"https://www.econdb.com/api/companies/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
companies()

import requests
                
def maritime_vessels():
    api_url = f"https://www.econdb.com/api/maritime/vessels/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
maritime_vessels()

import requests
                
def maritime_ports():
    api_url = f"https://www.econdb.com/api/maritime/ports/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
maritime_ports()

import requests
                
def retail_items():
    api_url = f"https://www.econdb.com/api/retail/items/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retail_items()

