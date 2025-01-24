import requests
                
def get_random_image():
    api_url = f"https://random-d.uk/api/random"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_image()

import requests
                
def get_quack_image():
    api_url = f"https://random-d.uk/api/quack"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_quack_image()

import requests
                
def get_random_image_file():
    api_url = f"https://random-d.uk/api/randomimg"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_image_file()

import requests
                
def get_list_of_images():
    api_url = f"https://random-d.uk/api/list"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_list_of_images()

import requests
                
def get_specific_image(num):
    api_url = f"https://random-d.uk/api/:num.jpg"
    querystring = {'num': num, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_specific_image(51)

import requests
                
def get_specific_gif(num):
    api_url = f"https://random-d.uk/api/:num.gif"
    querystring = {'num': num, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_specific_gif(12)

import requests
                
def get_http_status_code_image(code):
    api_url = f"https://random-d.uk/api/http/:code"
    querystring = {'code': code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_http_status_code_image(404)

import requests
                
def upload_image():
    api_url = f"https://random-d.uk/add"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
upload_image()

