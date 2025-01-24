import requests
                
def get_random_quote():
    api_url = f"https://ron-swanson-quotes.herokuapp.com/v2/quotes"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_quote()

import requests
                
def get_multiple_quotes(count):
    api_url = f"https://ron-swanson-quotes.herokuapp.com/v2/quotes/{count}"
    querystring = {'count': count, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_multiple_quotes(2)

import requests
                
def search_quotes(term):
    api_url = f"https://ron-swanson-quotes.herokuapp.com/v2/quotes/search/{term}"
    querystring = {'term': term, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_quotes('hate')

