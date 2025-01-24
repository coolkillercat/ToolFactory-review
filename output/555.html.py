import requests
                
def get_list_of_abilities():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_abilities()

import requests
                
def get_detail_of_ability(ability):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'ability': ability, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_ability('overgrow')

import requests
                
def get_list_of_berries():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_berries()

import requests
                
def get_detail_of_berry(berry):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'berry': berry, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_berry('cheri')

import requests
                
def get_list_of_egg_groups():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_egg_groups()

import requests
                
def get_detail_of_egg_group(eggGroup):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'eggGroup': eggGroup, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_egg_group('monster')

import requests
                
def get_list_of_encounter_methods():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_encounter_methods()

import requests
                
def get_detail_of_encounter_method(encounterMethod):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'encounterMethod': encounterMethod, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_encounter_method('walk')

import requests
                
def get_list_of_evolution_chains():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_evolution_chains()

import requests
                
def get_detail_of_evolution_chain(id):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'id': id, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_evolution_chain(1)

import requests
                
def get_list_of_evolution_triggers():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_evolution_triggers()

import requests
                
def get_detail_of_evolution_trigger(name):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'name': name, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_evolution_trigger('level-up')

import requests
                
def get_list_of_genders():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_genders()

import requests
                
def get_detail_of_gender(gender):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'gender': gender, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_gender('male')

import requests
                
def get_list_of_growth_rates():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_growth_rates()

import requests
                
def get_detail_of_growth_rate(growthRate):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'growthRate': growthRate, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_growth_rate('medium')

import requests
                
def get_list_of_locations():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_locations()

import requests
                
def get_detail_of_location(location):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'location': location, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_location('pallet-town')

import requests
                
def get_list_of_moves():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_moves()

import requests
                
def get_detail_of_move(move):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'move': move, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_move('tackle')

import requests
                
def get_list_of_natures():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_natures()

import requests
                
def get_detail_of_nature(nature):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'nature': nature, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_nature('adamant')

import requests
                
def get_list_of_pokemons():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_pokemons()

import requests
                
def get_detail_info_of_pokemon(name):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'name': name, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_info_of_pokemon('ditto')

import requests
                
def get_list_of_regions():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_regions()

import requests
                
def get_detail_of_region(region):
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {'region': region, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_detail_of_region('kanto')

import requests
                
def get_list_of_species():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_species()

import requests
                
def get_list_of_types():
    api_url = f"https://graphql-pokeapi.vercel.app/api/graphql"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_types()

