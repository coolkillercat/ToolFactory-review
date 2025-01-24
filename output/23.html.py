import requests
                
def list_documents():
    api_url = f"missing"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_documents()

import requests
                
def get_specific_document(documentId):
    api_url = f"missing"
    querystring = {'documentId': documentId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_specific_document('12345')

import requests
                
def get_document_part(documentId, partId):
    api_url = f"missing"
    querystring = {'documentId': documentId, 'partId': partId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_document_part('12345', 'section-1')

import requests
                
def search_documents(searchTerm):
    api_url = f"missing"
    querystring = {'searchTerm': searchTerm, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_documents('bylaw')

import requests
                
def search_document_part(searchTerm, partId):
    api_url = f"missing"
    querystring = {'searchTerm': searchTerm, 'partId': partId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_document_part('zoning', 'section-1')

