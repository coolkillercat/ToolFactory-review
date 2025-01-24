import requests
                
def all_leagues_available():
    api_url = f"https://api-football-standings.azharimm.site/leagues"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
all_leagues_available()

import requests
                
def league_detail(id):
    api_url = f"https://api-football-standings.azharimm.site/leagues/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
league_detail('eng.1')

import requests
                
def seasons_available(id):
    api_url = f"https://api-football-standings.azharimm.site/leagues/{id}/seasons"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
seasons_available('eng.1')

import requests
                
def standings(id):
    api_url = f"https://api-football-standings.azharimm.site/leagues/{id}/standings"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
standings('eng.1')

