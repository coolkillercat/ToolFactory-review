import requests
                
def get_random_neko_image():
    api_url = f"https://nekos.best/api/v1/neko"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_neko_image()

import requests
                
def get_random_neko_gif():
    api_url = f"https://nekos.best/api/v1/neko_gif"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_neko_gif()

import requests
                
def get_random_waifu_image():
    api_url = f"https://nekos.best/api/v1/waifu"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_waifu_image()

import requests
                
def get_random_waifu_gif():
    api_url = f"https://nekos.best/api/v1/waifu_gif"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_waifu_gif()

