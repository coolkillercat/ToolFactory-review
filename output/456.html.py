import requests
                
def get_character_by_id(id):
    api_url = f"https://anapioficeandfire.com/api/characters/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_character_by_id(583)

import requests
                
def get_book_by_id(id):
    api_url = f"https://anapioficeandfire.com/api/books/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_book_by_id(1)

import requests
                
def get_house_by_id(id):
    api_url = f"https://anapioficeandfire.com/api/houses/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_house_by_id(378)

