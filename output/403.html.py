import requests
                
def get_random_quote():
    api_url = f"https://the-dune-api.herokuapp.com/quotes"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_quote()

import requests
                
def get_multiple_quotes(number):
    api_url = f"https://the-dune-api.herokuapp.com/quotes/{number}"
    querystring = {'number': number, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_multiple_quotes(3)

import requests
                
def get_quote_by_id(id):
    api_url = f"https://the-dune-api.herokuapp.com/quotes/id/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_quote_by_id('66')

import requests
                
def get_random_book():
    api_url = f"https://the-dune-api.herokuapp.com/books"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_book()

import requests
                
def get_multiple_books(number):
    api_url = f"https://the-dune-api.herokuapp.com/books/{number}"
    querystring = {'number': number, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_multiple_books(3)

import requests
                
def get_book_by_id(id):
    api_url = f"https://the-dune-api.herokuapp.com/books/id/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_book_by_id('1')

