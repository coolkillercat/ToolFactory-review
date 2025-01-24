import requests
                
def get_random_genre():
    api_url = f"https://binaryjazz.us/wp-json/genrenator/v1/genre/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_genre()

import requests
                
def get_random_genre_story():
    api_url = f"https://binaryjazz.us/wp-json/genrenator/v1/story/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_genre_story()

