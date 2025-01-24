import requests
                
def normalized_data():
    api_url = f"https://share.osf.io/api/v2/normalizeddata/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
normalized_data()

import requests
                
def raw_data():
    api_url = f"https://share.osf.io/api/v2/rawdata/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
raw_data()

import requests
                
def source_registrations():
    api_url = f"https://share.osf.io/api/v2/sourceregistrations/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
source_registrations()

import requests
                
def sources():
    api_url = f"https://share.osf.io/api/v2/sources/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
sources()

import requests
                
def users():
    api_url = f"https://share.osf.io/api/v2/user/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
users()

import requests
                
def schema():
    api_url = f"https://share.osf.io/api/v2/schema/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
schema()

import requests
                
def status():
    api_url = f"https://share.osf.io/api/v2/status"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
status()

import requests
                
def rss_feed():
    api_url = f"https://share.osf.io/api/v2/rss"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
rss_feed()

import requests
                
def atom_feed():
    api_url = f"https://share.osf.io/api/v2/atom"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
atom_feed()

