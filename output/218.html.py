import requests
                
def get_color_names(values):
    api_url = f"https://api.color.pizza/v1/"
    querystring = {'values': values, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_color_names('aaffcc,0d0d0f,f39d91')

import requests
                
def get_supported_color_name_lists():
    api_url = f"https://api.color.pizza/v1/lists/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_supported_color_name_lists()

