import requests
                
def get_simple_square_image(size):
    api_url = f"https://www.placemonkeys.com/{size}"
    querystring = {'size': size, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_simple_square_image(500)

import requests
                
def get_custom_size_image(width, height):
    api_url = f"https://www.placemonkeys.com/{width}/{height}"
    querystring = {'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_custom_size_image(500, 350)

import requests
                
def get_greyscale_image(width, height):
    api_url = f"https://www.placemonkeys.com/{width}/{height}?greyscale"
    querystring = {'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_greyscale_image(500, 350)

import requests
                
def get_sepia_image(width, height):
    api_url = f"https://www.placemonkeys.com/{width}/{height}?sepia"
    querystring = {'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_sepia_image(500, 350)

import requests
                
def get_blurred_image(width, height):
    api_url = f"https://www.placemonkeys.com/{width}/{height}?blur={amount}"
    querystring = {'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_blurred_image(500, 350)

import requests
                
def get_spooky_image(width, height):
    api_url = f"https://www.placemonkeys.com/{width}/{height}?spooky"
    querystring = {'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_spooky_image(500, 350)

import requests
                
def get_random_image(width, height):
    api_url = f"https://www.placemonkeys.com/{width}/{height}?random={value}"
    querystring = {'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_image(500, 350)

