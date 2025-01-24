import requests
                
def get_fruit_data_by_id(ID):
    api_url = f"/api/fruit/{ID}"
    querystring = {'ID': ID, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_fruit_data_by_id('1')

import requests
                
def get_fruit_data_by_name(name):
    api_url = f"/api/fruit/{name}"
    querystring = {'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_fruit_data_by_name('apple')

