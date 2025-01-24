import requests
                
def get_a_random_pun():
    api_url = f"https://punapi.rest/api/pun"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_random_pun()

import requests
                
def get_pun_by_id(id):
    api_url = f"https://punapi.rest/api/pun?id={id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_pun_by_id(2)

import requests
                
def get_puns_by_pagination(page):
    api_url = f"https://punapi.rest/api/pun/pagination?page={page}"
    querystring = {'page': page, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_puns_by_pagination(2)

import requests
                
def get_puns_by_searching(query):
    api_url = f"https://punapi.rest/api/pun/search?query={query}"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_puns_by_searching('cookie')

import requests
                
def get_pun_meme():
    api_url = f"https://punapi.rest/api/meme"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_pun_meme()

