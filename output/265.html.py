import requests
                
def server_statistics():
    api_url = f"https://ch.tetr.io/api/general/stats"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
server_statistics()

import requests
                
def server_activity():
    api_url = f"https://ch.tetr.io/api/general/activity"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
server_activity()

import requests
                
def user_info(_user):
    api_url = f"https://ch.tetr.io/api/users/:user"
    querystring = {'_user': _user, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
user_info(exampleUser)

import requests
                
def user_records(_user):
    api_url = f"https://ch.tetr.io/api/users/:user/records"
    querystring = {'_user': _user, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
user_records(exampleUser)

import requests
                
def user_search(_query):
    api_url = f"https://ch.tetr.io/api/users/search/:query"
    querystring = {'_query': _query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
user_search('123456789012345678')

import requests
                
def tetra_league_leaderboard():
    api_url = f"https://ch.tetr.io/api/users/lists/league"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
tetra_league_leaderboard()

import requests
                
def tetra_league_leaderboard__full_export_():
    api_url = f"https://ch.tetr.io/api/users/lists/league/all"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
tetra_league_leaderboard__full_export_()

import requests
                
def xp_leaderboard():
    api_url = f"https://ch.tetr.io/api/users/lists/xp"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
xp_leaderboard()

import requests
                
def get_stream(_stream):
    api_url = f"https://ch.tetr.io/api/streams/:stream"
    querystring = {'_stream': _stream, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_stream('40l_global')

import requests
                
def all_latest_news():
    api_url = f"https://ch.tetr.io/api/news/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
all_latest_news()

import requests
                
def latest_news(_stream):
    api_url = f"https://ch.tetr.io/api/news/:stream"
    querystring = {'_stream': _stream, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
latest_news('global')

