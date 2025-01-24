import requests
                
def get_all_characters():
    api_url = f"https://api-blue-archive.vercel.app/api/characters"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_characters()

import requests
                
def get_characters_by_name():
    api_url = f"https://api-blue-archive.vercel.app/api/characters"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_characters_by_name()

import requests
                
def get_random_character():
    api_url = f"https://api-blue-archive.vercel.app/api/character/random"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_character()

import requests
                
def get_all_students():
    api_url = f"https://api-blue-archive.vercel.app/api/characters/students"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_students()

