import requests
                
def get_all_digimon():
    api_url = f"https://digimon-api.vercel.app/api/digimon"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_digimon()

import requests
                
def get_digimon_by_name(name):
    api_url = f"https://digimon-api.vercel.app/api/digimon/name/:name"
    querystring = {'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_digimon_by_name('agumon')

import requests
                
def get_digimon_by_level(level):
    api_url = f"https://digimon-api.vercel.app/api/digimon/level/:level"
    querystring = {'level': level, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_digimon_by_level('rookie')

