import requests
                
def search_newspaper_titles(terms):
    api_url = f"https://chroniclingamerica.loc.gov/search/titles/results/"
    querystring = {'terms': terms, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_newspaper_titles('michigan')

import requests
                
def search_newspaper_pages(andtext):
    api_url = f"https://chroniclingamerica.loc.gov/search/pages/results/"
    querystring = {'andtext': andtext, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_newspaper_pages('thomas')

import requests
                
def autosuggest_newspaper_titles(q):
    api_url = f"https://chroniclingamerica.loc.gov/suggest/titles/"
    querystring = {'q': q, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
autosuggest_newspaper_titles('Florida')

import requests
                
def json_views(resource):
    api_url = f"missing"
    querystring = {'resource': resource, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
json_views('lccn/sn86069873.json')

import requests
                
def bulk_data_access():
    api_url = f"https://chroniclingamerica.loc.gov/data/batches/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
bulk_data_access()

import requests
                
def cors_and_jsonp_support(q):
    api_url = f"https://chroniclingamerica.loc.gov/suggest/titles/"
    querystring = {'q': q, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
cors_and_jsonp_support('manh')

