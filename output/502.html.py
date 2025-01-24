import requests
                
def avatars(uuid):
    api_url = f"https://crafatar.com/avatars/{uuid}"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
avatars('853c80ef3c3749fdaa49938b674adae6')

import requests
                
def head_renders(uuid):
    api_url = f"https://crafatar.com/renders/head/{uuid}"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
head_renders('853c80ef3c3749fdaa49938b674adae6')

import requests
                
def body_renders(uuid):
    api_url = f"https://crafatar.com/renders/body/{uuid}"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
body_renders('853c80ef3c3749fdaa49938b674adae6')

import requests
                
def skins(uuid):
    api_url = f"https://crafatar.com/skins/{uuid}"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
skins('853c80ef3c3749fdaa49938b674adae6')

import requests
                
def capes(uuid):
    api_url = f"https://crafatar.com/capes/{uuid}"
    querystring = {'uuid': uuid, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
capes('853c80ef3c3749fdaa49938b674adae6')

