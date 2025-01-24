import requests
                
def get_all_licenses():
    api_url = f"https://licenseapi.herokuapp.com/licenses"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_licenses()

import requests
                
def get_single_license(id):
    api_url = f"https://licenseapi.herokuapp.com/licenses/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_single_license('gpl-3.0')

import requests
                
def get_rules():
    api_url = f"https://licenseapi.herokuapp.com/rules"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_rules()

import requests
                
def get_api_version():
    api_url = f"https://licenseapi.herokuapp.com/version"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_api_version()

import requests
                
def get_api_status():
    api_url = f"https://licenseapi.herokuapp.com/status"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_api_status()

