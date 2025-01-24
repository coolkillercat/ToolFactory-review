import requests
                
def estimate_age_from_name(name):
    api_url = f"https://api.agify.io"
    querystring = {'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
estimate_age_from_name('Michael')

import requests
                
def classify_gender_from_name(name):
    api_url = f"https://api.genderize.io"
    querystring = {'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
classify_gender_from_name('Emily')

import requests
                
def predict_nationality_from_name(name):
    api_url = f"https://api.nationalize.io"
    querystring = {'name': name, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
predict_nationality_from_name('Hiroshi')

