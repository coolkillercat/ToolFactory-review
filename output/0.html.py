import requests
                
def create_a_session():
    api_url = f"https://connectfourapi.com/api/create"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_a_session()

import requests
                
def connect_to_a_session(sessionid):
    api_url = f"https://connectfourapi.com/api/{sessionid}/connect"
    querystring = {'sessionid': sessionid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
connect_to_a_session('abc123')

import requests
                
def join_a_session(sessionid, name):
    api_url = f"https://connectfourapi.com/api/{sessionid}/{name}/join"
    querystring = {'sessionid': sessionid, 'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
join_a_session('abc123', 'Player1')

import requests
                
def start_the_game(sessionid):
    api_url = f"https://connectfourapi.com/api/{sessionid}/start"
    querystring = {'sessionid': sessionid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
start_the_game('abc123')

import requests
                
def drop_piece(sessionid, name, column):
    api_url = f"https://connectfourapi.com/api/{sessionid}/{name}/{column}/drop"
    querystring = {'sessionid': sessionid, 'name': name, 'column': column, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
drop_piece('abc123', 'Player1', 3)

import requests
                
def delete_a_session(sessionid):
    api_url = f"https://connectfourapi.com/api/{sessionid}/delete"
    querystring = {'sessionid': sessionid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
delete_a_session('abc123')

import requests
                
def leave_a_table(sessionid, name):
    api_url = f"https://connectfourapi.com/api/{sessionid}/{name}/leave"
    querystring = {'sessionid': sessionid, 'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
leave_a_table('abc123', 'Player1')

