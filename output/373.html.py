import requests
                
def get_all_quotes():
    api_url = f"http://localhost:5000/quotes"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_quotes()

import requests
                
def get_random_quote():
    api_url = f"http://localhost:5000/quotes/random"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_quote()

import requests
                
def get_quote_by_id(id):
    api_url = f"http://localhost:5000/quotes/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_quote_by_id('5a6ce86f2af929789500e824')

import requests
                
def get_quote_by_author(author):
    api_url = f"http://localhost:5000/quotes/author/{author}"
    querystring = {'author': author, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_quote_by_author('Edsger W. Dijkstra')

import requests
                
def create_quote(quote, author):
    api_url = f"missing"
    payload = {'quote': quote, 'author': author, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_quote('Code is like humor. When you have to explain it, it’s bad.', 'Cory House')

