import requests
                
def get_domains():
    api_url = f"https://api.mail.tm/domains"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_domains()

import requests
                
def get_domain_by_id(id):
    api_url = f"https://api.mail.tm/domains/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_domain_by_id('12345')

import requests
                
def create_account(address, password):
    api_url = f"https://api.mail.tm/accounts"
    payload = {'address': address, 'password': password, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_account('user@example.com', 'password123')

import requests
                
def get_account_by_id(id):
    api_url = f"https://api.mail.tm/accounts/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_account_by_id('12345')

import requests
                
def get_current_account():
    api_url = f"https://api.mail.tm/me"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_current_account()

import requests
                
def get_messages():
    api_url = f"https://api.mail.tm/messages"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_messages()

import requests
                
def get_message_by_id(id):
    api_url = f"https://api.mail.tm/messages/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_message_by_id('12345')

import requests
                
def get_message_source(id):
    api_url = f"https://api.mail.tm/sources/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_message_source('12345')

