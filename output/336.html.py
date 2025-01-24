import requests
                
def endpoints_data():
    api_url = f"https://finalspaceapi.com/api/v0/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
endpoints_data()

import requests
                
def all_characters():
    api_url = f"https://finalspaceapi.com/api/v0/character"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
all_characters()

import requests
                
def single_character(id):
    api_url = f"https://finalspaceapi.com/api/v0/character/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
single_character('1')

import requests
                
def all_episodes():
    api_url = f"https://finalspaceapi.com/api/v0/episode"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
all_episodes()

import requests
                
def single_episode(id):
    api_url = f"https://finalspaceapi.com/api/v0/episode/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
single_episode('1')

import requests
                
def all_locations():
    api_url = f"https://finalspaceapi.com/api/v0/location"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
all_locations()

import requests
                
def single_location(id):
    api_url = f"https://finalspaceapi.com/api/v0/location/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
single_location('1')

import requests
                
def all_quotes():
    api_url = f"https://finalspaceapi.com/api/v0/quote"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
all_quotes()

