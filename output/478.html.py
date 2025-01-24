import requests
                
def get_amiibo_by_name(name):
    api_url = f"https://www.amiiboapi.com/api/amiibo/?name={name}"
    querystring = {'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_amiibo_by_name('mario')

import requests
                
def get_amiibo_by_game_series(gameseries):
    api_url = f"https://www.amiiboapi.com/api/amiibo/?gameseries={gameseries}"
    querystring = {'gameseries': gameseries, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_amiibo_by_game_series('zelda')

import requests
                
def get_amiibo_by_character(character):
    api_url = f"https://www.amiiboapi.com/api/amiibo/?character={character}"
    querystring = {'character': character, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_amiibo_by_character('zelda')

