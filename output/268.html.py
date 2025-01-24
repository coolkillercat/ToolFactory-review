import requests
                
def get_person(id):
    api_url = f"https://swapi.dev/api/people/{id}/"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_person(1)

import requests
                
def get_planet(id):
    api_url = f"https://swapi.dev/api/planets/{id}/"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_planet(3)

import requests
                
def get_starship(id):
    api_url = f"https://swapi.dev/api/starships/{id}/"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_starship(9)

