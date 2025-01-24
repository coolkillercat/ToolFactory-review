import requests
                
def get_current_comic():
    api_url = f"https://xkcd.com/info.0.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_current_comic()

import requests
                
def get_specific_comic(comic_number):
    api_url = f"https://xkcd.com/{comic_number}/info.0.json"
    querystring = {'comic_number': comic_number, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_specific_comic(614)

