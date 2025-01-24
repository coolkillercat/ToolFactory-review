import requests
                
def get_a_random_quote():
    api_url = f"https://api.gameofthronesquotes.xyz/v1/random"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_a_random_quote()

import requests
                
def get_several_random_quotes():
    api_url = f"https://api.gameofthronesquotes.xyz/v1/random/5"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_several_random_quotes()

import requests
                
def get_quotes_from_a_character():
    api_url = f"https://api.gameofthronesquotes.xyz/v1/author/tyrion/2"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_quotes_from_a_character()

import requests
                
def list_of_houses_with_their_members():
    api_url = f"https://api.gameofthronesquotes.xyz/v1/houses"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_of_houses_with_their_members()

import requests
                
def get_house_s_details():
    api_url = f"https://api.gameofthronesquotes.xyz/v1/house/lannister"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_house_s_details()

import requests
                
def list_of_characters_with_their_quotes():
    api_url = f"https://api.gameofthronesquotes.xyz/v1/characters"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_of_characters_with_their_quotes()

import requests
                
def get_character_s_details_with_his_quotes():
    api_url = f"https://api.gameofthronesquotes.xyz/v1/character/jon"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_character_s_details_with_his_quotes()

