import requests
                
def get_random_quote():
    api_url = f"https://moviequote.onrender.com/v1/quote/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_quote()

import requests
                
def get_random_quote__censored_():
    api_url = f"https://moviequote.onrender.com/v1/quote?censored"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_quote__censored_()

import requests
                
def get_random_quote_from_show(show_slug):
    api_url = f"https://moviequote.onrender.com/v1/shows/{show_slug}"
    querystring = {'show_slug': show_slug, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_quote_from_show('breaking-bad')

import requests
                
def get_list_of_shows():
    api_url = f"https://moviequote.onrender.com/v1/shows/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_shows()

