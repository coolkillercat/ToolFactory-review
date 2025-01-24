import requests
                
def get_all_cards():
    api_url = f"https://protected-taiga-89091.herokuapp.com/api/card"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_cards()

import requests
                
def get_card_by_id(id):
    api_url = f"https://protected-taiga-89091.herokuapp.com/api/card/:id"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_card_by_id('6039396a68347a4a842920cf')

