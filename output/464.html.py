import requests
                
def get_random_color_palette(model):
    api_url = f"http://colormind.io/api/"
    payload = {'model': 'default', }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_color_palette('default')

import requests
                
def get_color_suggestions(input, model):
    api_url = f"http://colormind.io/api/"
    payload = {'input': input, 'model': 'default', }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_color_suggestions([[44,43,44],[90,83,82],'N','N','N'], 'default')

import requests
                
def list_available_models():
    api_url = f"http://colormind.io/list/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_available_models()

