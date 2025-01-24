import requests
                
def create_gotiny_link(input):
    api_url = f"https://gotiny.cc/api"
    payload = {'input': input, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_gotiny_link('https://amazon.com/very-long-url')

import requests
                
def resolve_gotiny_link(code):
    api_url = f"https://gotiny.cc/api/{code}"
    querystring = {'code': code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
resolve_gotiny_link('y68hxc')

