import requests
                
def minecraft_account_lookup(ID):
    api_url = f"https://playerdb.co/api/player/minecraft/$ID"
    querystring = {'ID': ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
minecraft_account_lookup('Notch')

import requests
                
def steam_account_lookup(ID):
    api_url = f"https://playerdb.co/api/player/steam/$ID"
    querystring = {'ID': ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
steam_account_lookup('76561197960435530')

import requests
                
def xbox_account_lookup(ID):
    api_url = f"https://playerdb.co/api/player/xbox/$ID"
    querystring = {'ID': ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
xbox_account_lookup('MajorNelson')

