import requests
                
def fetch_a_random_dad_joke():
    api_url = f"https://icanhazdadjoke.com/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_a_random_dad_joke()

import requests
                
def fetch_a_random_dad_joke_as_a_slack_message():
    api_url = f"https://icanhazdadjoke.com/slack"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_a_random_dad_joke_as_a_slack_message()

import requests
                
def fetch_a_dad_joke(joke_id):
    api_url = f"https://icanhazdadjoke.com/j/{joke_id}"
    querystring = {'joke_id': joke_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_a_dad_joke('R7UfaahVfFd')

import requests
                
def fetch_a_dad_joke_as_an_image(joke_id):
    api_url = f"https://icanhazdadjoke.com/j/{joke_id}.png"
    querystring = {'joke_id': joke_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_a_dad_joke_as_an_image('R7UfaahVfFd')

import requests
                
def search_for_dad_jokes():
    api_url = f"https://icanhazdadjoke.com/search"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_for_dad_jokes()

import requests
                
def graphql_api(query):
    api_url = f"https://icanhazdadjoke.com/graphql"
    payload = {'query': query, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
graphql_api('{"query": "query { joke {id joke permalink } }"}')

