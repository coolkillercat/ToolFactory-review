import requests
                
def get_users():
    api_url = f"https://24pullrequests.com/users.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_users()

import requests
                
def get_user(username):
    api_url = f"https://24pullrequests.com/users/{username}.json"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_user('andrew')

import requests
                
def get_projects():
    api_url = f"https://24pullrequests.com/projects.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_projects()

import requests
                
def get_contributions():
    api_url = f"https://24pullrequests.com/pull_requests.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_contributions()

import requests
                
def get_contributions_meta():
    api_url = f"https://24pullrequests.com/pull_requests/meta.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_contributions_meta()

import requests
                
def get_organisations():
    api_url = f"https://24pullrequests.com/organisations.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_organisations()

import requests
                
def get_organisation(organisation):
    api_url = f"https://24pullrequests.com/organisations/{organisation}.json"
    querystring = {'organisation': organisation, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_organisation('uswitch')

