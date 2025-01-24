import requests
                
def get_card_information():
    api_url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_card_information()

import requests
                
def random_card():
    api_url = f"https://db.ygoprodeck.com/api/v7/randomcard.php"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
random_card()

import requests
                
def all_card_sets():
    api_url = f"https://db.ygoprodeck.com/api/v7/cardsets.php"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
all_card_sets()

import requests
                
def card_set_information(setcode):
    api_url = f"https://db.ygoprodeck.com/api/v7/cardsetsinfo.php"
    querystring = {'setcode': setcode, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
card_set_information('SDY-046')

import requests
                
def all_card_archetypes():
    api_url = f"https://db.ygoprodeck.com/api/v7/archetypes.php"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
all_card_archetypes()

import requests
                
def check_database_version():
    api_url = f"https://db.ygoprodeck.com/api/v7/checkDBVer.php"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
check_database_version()

