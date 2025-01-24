import requests
                
def get_all_objects():
    api_url = f"https://rps101.pythonanywhere.com/api/v1/objects/all"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_objects()

import requests
                
def get_object_outcomes(object_name):
    api_url = f"https://rps101.pythonanywhere.com/api/v1/objects/{object name}"
    querystring = {'object_name': object_name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_object_outcomes('nuke')

import requests
                
def get_match_result(object_one, object_two):
    api_url = f"https://rps101.pythonanywhere.com/api/v1/match"
    querystring = {'object_one': object_one, 'object_two': object_two, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_match_result('nuke', 'tank')

