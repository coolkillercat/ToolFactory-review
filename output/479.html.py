import requests
                
def shuffle_the_cards():
    api_url = f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
shuffle_the_cards()

import requests
                
def draw_a_card(deck_id):
    api_url = f"https://deckofcardsapi.com/api/deck/{{deck_id}}/draw/?count=2"
    querystring = {'deck_id': deck_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
draw_a_card('3p40paa87x90')

import requests
                
def reshuffle_the_cards(deck_id):
    api_url = f"https://deckofcardsapi.com/api/deck/{{deck_id}}/shuffle/?remaining=true"
    querystring = {'deck_id': deck_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
reshuffle_the_cards('3p40paa87x90')

import requests
                
def a_brand_new_deck():
    api_url = f"https://deckofcardsapi.com/api/deck/new/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
a_brand_new_deck()

import requests
                
def a_partial_deck():
    api_url = f"https://deckofcardsapi.com/api/deck/new/shuffle/?cards=AS,2S,KS,AD,2D,KD,AC,2C,KC,AH,2H,KH"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
a_partial_deck()

import requests
                
def adding_to_piles(deck_id, pile_name):
    api_url = f"https://deckofcardsapi.com/api/deck/{{deck_id}}/pile/{{pile_name}}/add/?cards=AS,2S"
    querystring = {'deck_id': deck_id, 'pile_name': pile_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
adding_to_piles('3p40paa87x90', 'discard')

import requests
                
def shuffle_piles(deck_id, pile_name):
    api_url = f"https://deckofcardsapi.com/api/deck/{{deck_id}}/pile/{{pile_name}}/shuffle/"
    querystring = {'deck_id': deck_id, 'pile_name': pile_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
shuffle_piles('3p40paa87x90', 'discard')

import requests
                
def listing_cards_in_piles(deck_id, pile_name):
    api_url = f"https://deckofcardsapi.com/api/deck/{{deck_id}}/pile/{{pile_name}}/list/"
    querystring = {'deck_id': deck_id, 'pile_name': pile_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
listing_cards_in_piles('3p40paa87x90', 'player1')

import requests
                
def drawing_from_piles(deck_id, pile_name):
    api_url = f"https://deckofcardsapi.com/api/deck/{{deck_id}}/pile/{{pile_name}}/draw/?cards=AS"
    querystring = {'deck_id': deck_id, 'pile_name': pile_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
drawing_from_piles('3p40paa87x90', 'discard')

import requests
                
def returning_cards_to_the_deck(deck_id):
    api_url = f"https://deckofcardsapi.com/api/deck/{{deck_id}}/return/?cards=AS,2S"
    querystring = {'deck_id': deck_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
returning_cards_to_the_deck('3p40paa87x90')

