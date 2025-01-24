import requests
                
def application_json():
    api_url = f"https://earthquake.usgs.gov/fdsnws/event/1/application.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
application_json()

import requests
                
def application_wadl():
    api_url = f"https://earthquake.usgs.gov/fdsnws/event/1/application.wadl"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
application_wadl()

import requests
                
def catalogs():
    api_url = f"https://earthquake.usgs.gov/fdsnws/event/1/catalogs"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
catalogs()

import requests
                
def contributors():
    api_url = f"https://earthquake.usgs.gov/fdsnws/event/1/contributors"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
contributors()

import requests
                
def count():
    api_url = f"https://earthquake.usgs.gov/fdsnws/event/1/count"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
count()

import requests
                
def query():
    api_url = f"https://earthquake.usgs.gov/fdsnws/event/1/query"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query()

import requests
                
def version():
    api_url = f"https://earthquake.usgs.gov/fdsnws/event/1/version"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
version()

