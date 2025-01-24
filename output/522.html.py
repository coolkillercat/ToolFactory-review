import requests
                
def get_card_data(id):
    api_url = f"https://api.scryfall.com/cards/:id"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_card_data('12345')

import requests
                
def search_cards(q):
    api_url = f"https://api.scryfall.com/cards/search"
    querystring = {'q': q, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_cards('goblin')

import requests
                
def get_bulk_data():
    api_url = f"https://api.scryfall.com/bulk-data"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_bulk_data()

