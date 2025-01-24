import requests
                
def check_gender_of_a_name(name):
    api_url = f"https://api.genderize.io"
    querystring = {'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
check_gender_of_a_name('John')

import requests
                
def batch_gender_prediction(names):
    api_url = f"https://api.genderize.io"
    payload = {'names': names, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
batch_gender_prediction(['John', 'Jane'])

