import requests
                
def get_random_emoji():
    api_url = f"https://emojihub.yurace.pro/api/random"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_emoji()

import requests
                
def get_all_emojis():
    api_url = f"https://emojihub.yurace.pro/api/all"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_emojis()

import requests
                
def get_emojis_by_category(category_name):
    api_url = f"https://emojihub.yurace.pro/api/all/category/{category-name}"
    querystring = {'category_name': category_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_emojis_by_category('food-and-drink')

import requests
                
def get_emojis_by_group(group_name):
    api_url = f"https://emojihub.yurace.pro/api/all/group/{group-name}"
    querystring = {'group_name': group_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_emojis_by_group('face-positive')

