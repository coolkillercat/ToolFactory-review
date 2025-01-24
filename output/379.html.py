import requests
                
def retrieve_a_random_chuck_norris_joke():
    api_url = f"https://api.chucknorris.io/jokes/random"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_a_random_chuck_norris_joke()

import requests
                
def retrieve_a_random_chuck_norris_joke_from_a_given_category(category):
    api_url = f"https://api.chucknorris.io/jokes/random?category={category}"
    querystring = {'category': category, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_a_random_chuck_norris_joke_from_a_given_category('animal')

import requests
                
def retrieve_a_list_of_available_categories():
    api_url = f"https://api.chucknorris.io/jokes/categories"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
retrieve_a_list_of_available_categories()

import requests
                
def free_text_search(query):
    api_url = f"https://api.chucknorris.io/jokes/search?query={query}"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
free_text_search('roundhouse')

