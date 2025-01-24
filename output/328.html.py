import requests
                
def objects():
    api_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
objects()

import requests
                
def object(objectID):
    api_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/[objectID]"
    querystring = {'objectID': objectID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
object(437133)

import requests
                
def departments():
    api_url = f"https://collectionapi.metmuseum.org/public/collection/v1/departments"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
departments()

import requests
                
def search(q):
    api_url = f"https://collectionapi.metmuseum.org/public/collection/v1/search"
    querystring = {'q': q, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search('sunflowers')

