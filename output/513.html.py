import requests
                
def get_all_networks():
    api_url = f"http://api.citybik.es/v2/networks"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_networks()

import requests
                
def get_network_by_id(network_id):
    api_url = f"http://api.citybik.es/v2/networks/{network_id}"
    querystring = {'network_id': network_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_network_by_id('velib')

