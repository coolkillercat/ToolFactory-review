import requests
                
def request_json(id):
    api_url = f"https://json.extendsclass.com/bin/:id"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
request_json('12345')

import requests
                
def create_json():
    api_url = f"https://json.extendsclass.com/bin"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_json()

import requests
                
def request_all_bin_ids():
    api_url = f"https://json.extendsclass.com/bins"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
request_all_bin_ids()

