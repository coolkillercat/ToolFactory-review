import requests
                
def filter_stopping_words(input):
    api_url = f"missing"
    payload = {'input': input, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
filter_stopping_words('This is a sample text.')

import requests
                
def filter_stemming_words(input):
    api_url = f"missing"
    payload = {'input': input, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
filter_stemming_words('Connecting connections.')

import requests
                
def get_swear_words(input):
    api_url = f"missing"
    payload = {'input': input, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_swear_words('This is a sample text with swear words.')

