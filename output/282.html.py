import requests
                
def get_dataset_list():
    api_url = f"https://data.gov.ie/api/3/action/package_list"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_dataset_list()

import requests
                
def get_tag_list():
    api_url = f"https://data.gov.ie/api/3/action/tag_list"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_tag_list()

import requests
                
def show_package(id):
    api_url = f"https://data.gov.ie/api/3/action/package_show"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
show_package('the-walled-towns-of-ireland')

import requests
                
def show_tag(id):
    api_url = f"https://data.gov.ie/api/3/action/tag_show"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
show_tag('marine')

import requests
                
def search_packages(q):
    api_url = f"https://data.gov.ie/api/3/action/package_search"
    querystring = {'q': q, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_packages('museum')

import requests
                
def search_resources(query):
    api_url = f"https://data.gov.ie/api/3/action/resource_search"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_resources('name:The Walled Towns of Ireland')

