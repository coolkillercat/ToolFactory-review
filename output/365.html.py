import requests
                
def get_item_by_name(item_name):
    api_url = f"https://botw-compendium.herokuapp.com/api/v3/entry/{item_name}"
    querystring = {'item_name': item_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_item_by_name('white-maned_lynel')

import requests
                
def get_all_items_in_a_category(category_name):
    api_url = f"https://botw-compendium.herokuapp.com/api/v3/category/{category_name}"
    querystring = {'category_name': category_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_items_in_a_category('monsters')

import requests
                
def get_all_data():
    api_url = f"https://botw-compendium.herokuapp.com/api/v3/all"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_data()

