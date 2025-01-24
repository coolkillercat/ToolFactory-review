import requests
                
def get_garden_image_by_http_status_code(code):
    api_url = f"https://http.garden/[code].jpg"
    querystring = {'code': code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_garden_image_by_http_status_code('404')

import requests
                
def get_garden_image_by_http_status_code__webp_format_(code):
    api_url = f"https://http.garden/[code].webp"
    querystring = {'code': code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_garden_image_by_http_status_code__webp_format_('404')

import requests
                
def get_garden_image_by_http_status_code__jxl_format_(code):
    api_url = f"https://http.garden/[code].jxl"
    querystring = {'code': code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_garden_image_by_http_status_code__jxl_format_('404')

import requests
                
def get_garden_image_by_http_status_code__avif_format_(code):
    api_url = f"https://http.garden/[code].avif"
    querystring = {'code': code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_garden_image_by_http_status_code__avif_format_('404')

import requests
                
def get_garden_image_metadata_by_http_status_code(code):
    api_url = f"https://http.garden/[code].json"
    querystring = {'code': code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_garden_image_metadata_by_http_status_code('404')

