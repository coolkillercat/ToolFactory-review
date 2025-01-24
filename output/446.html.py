import requests
                
def thing_items(id):
    api_url = f"https://boardgamegeek.com/xmlapi2/thing?"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
thing_items('123,456')

import requests
                
def family_items(id):
    api_url = f"https://boardgamegeek.com/xmlapi2/family?"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
family_items('123,456')

import requests
                
def forum_lists(id):
    api_url = f"https://boardgamegeek.com/xmlapi2/forumlist?"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
forum_lists('123')

import requests
                
def forums(id):
    api_url = f"https://boardgamegeek.com/xmlapi2/forum?"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
forums('123')

import requests
                
def threads(id):
    api_url = f"https://boardgamegeek.com/xmlapi2/thread?"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
threads('123')

import requests
                
def users(name):
    api_url = f"https://boardgamegeek.com/xmlapi2/user?"
    querystring = {'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
users('john_doe')

import requests
                
def guilds(id):
    api_url = f"https://boardgamegeek.com/xmlapi2/guild?"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
guilds('123')

import requests
                
def plays():
    api_url = f"https://boardgamegeek.com/xmlapi2/plays?"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
plays()

import requests
                
def collection(username):
    api_url = f"https://boardgamegeek.com/xmlapi2/collection?"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
collection('john_doe')

