import requests
                
def get_article_content(action, page, format):
    api_url = f"https://www.example.org/w/api.php"
    querystring = {'action': action, 'page': page, 'format': 'json', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_article_content('parse', 'Pet_door', 'json')

import requests
                
def create_account(action, username, password, retype, createtoken, format):
    api_url = f"https://www.example.org/w/api.php"
    payload = {'action': action, 'username': username, 'password': password, 'retype': retype, 'createtoken': createtoken, 'format': 'json', }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_account('createaccount', 'newuser', 'password123', 'password123', '123ABC', 'json')

import requests
                
def login(action, lgname, lgpassword, format):
    api_url = f"https://www.example.org/w/api.php"
    payload = {'action': action, 'lgname': lgname, 'lgpassword': lgpassword, 'format': 'json', }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
login('login', 'user', 'password123', 'json')

import requests
                
def logout(action, format):
    api_url = f"https://www.example.org/w/api.php"
    payload = {'action': action, 'format': 'json', }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
logout('logout', 'json')

import requests
                
def query(action, format):
    api_url = f"https://www.example.org/w/api.php"
    querystring = {'action': action, 'format': 'json', }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
query('query', 'json')

