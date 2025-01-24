import requests
                
def dcat_catalog_search(q):
    api_url = f"https://ckan.govdata.de/api/3/action/dcat_catalog_search"
    querystring = {'q': q, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
dcat_catalog_search('kindergarten')

import requests
                
def govdata_api___rdf():
    api_url = f"https://www.govdata.de/ckan/catalog/catalog.rdf"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
govdata_api___rdf()

import requests
                
def govdata_api___turtle():
    api_url = f"https://www.govdata.de/ckan/catalog/catalog.ttl"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
govdata_api___turtle()

import requests
                
def govdata_api___json_ld():
    api_url = f"https://www.govdata.de/ckan/catalog/catalog.jsonld"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
govdata_api___json_ld()

import requests
                
def metadaten_rdf():
    api_url = f"https://www.govdata.de/ckan/dataset/govdata-metadatenkatalog.rdf"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
metadaten_rdf()

