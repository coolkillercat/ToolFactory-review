import requests
                
def get_all_anime():
    api_url = f"https://anime-facts-rest-api.herokuapp.com/api/v1"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_anime()

import requests
                
def get_anime_facts(anime_name):
    api_url = f"https://anime-facts-rest-api.herokuapp.com/api/v1/:anime_name"
    querystring = {'anime_name': anime_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_anime_facts('fma_brotherhood')

import requests
                
def get_specific_anime_fact(anime_name, fact_id):
    api_url = f"https://anime-facts-rest-api.herokuapp.com/api/v1/:anime_name/:fact_id"
    querystring = {'anime_name': anime_name, 'fact_id': fact_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_specific_anime_fact('fma_brotherhood', 2)

