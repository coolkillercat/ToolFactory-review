import requests
                
def get_random_image(width, height):
    api_url = f"https://picsum.photos/{width}/{height}"
    querystring = {'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_image(200, 300)

import requests
                
def get_square_image(size):
    api_url = f"https://picsum.photos/{size}"
    querystring = {'size': size, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_square_image(200)

import requests
                
def get_specific_image(image, width, height):
    api_url = f"https://picsum.photos/id/{image}/{width}/{height}"
    querystring = {'image': image, 'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_specific_image('237', 200, 300)

import requests
                
def get_static_random_image(seed, width, height):
    api_url = f"https://picsum.photos/seed/{seed}/{width}/{height}"
    querystring = {'seed': seed, 'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_static_random_image('picsum', 200, 300)

import requests
                
def get_grayscale_image(width, height):
    api_url = f"https://picsum.photos/{width}/{height}?grayscale"
    querystring = {'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_grayscale_image(200, 300)

import requests
                
def get_blurred_image(width, height):
    api_url = f"https://picsum.photos/{width}/{height}?blur"
    querystring = {'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_blurred_image(200, 300)

import requests
                
def list_images():
    api_url = f"https://picsum.photos/v2/list"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_images()

import requests
                
def get_image_details_by_id(id):
    api_url = f"https://picsum.photos/id/{id}/info"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_image_details_by_id('0')

import requests
                
def get_image_details_by_seed(seed):
    api_url = f"https://picsum.photos/seed/{seed}/info"
    querystring = {'seed': seed, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_image_details_by_seed('picsum')

