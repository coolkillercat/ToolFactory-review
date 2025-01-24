import requests
                
def get_pokémon_by_name_or_id(name_or_id):
    api_url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id}"
    querystring = {'name_or_id': name_or_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_pokémon_by_name_or_id('ditto')

import requests
                
def get_pokémon_species_by_name_or_id(name_or_id):
    api_url = f"https://pokeapi.co/api/v2/pokemon-species/{name_or_id}"
    querystring = {'name_or_id': name_or_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_pokémon_species_by_name_or_id('aegislash')

import requests
                
def get_pokémon_type_by_id(id):
    api_url = f"https://pokeapi.co/api/v2/type/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_pokémon_type_by_id(3)

import requests
                
def get_pokémon_ability_by_name(name):
    api_url = f"https://pokeapi.co/api/v2/ability/{name}"
    querystring = {'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_pokémon_ability_by_name('battle-armor')

import requests
                
def get_pokémon_list():
    api_url = f"https://pokeapi.co/api/v2/pokemon"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_pokémon_list()

