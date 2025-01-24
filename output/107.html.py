import requests
                
def get_user(userId):
    api_url = f"missing"
    querystring = {'userId': userId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_user('123')

import requests
                
def create_user(username, email):
    api_url = f"missing"
    payload = {'username': username, 'email': email, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_user('johndoe', 'johndoe@example.com')

