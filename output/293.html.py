import requests
                
def get_all_characters():
    api_url = f"https://puyodb-api-deno.herokuapp.com/api/v1/characters"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_characters()

import requests
                
def get_character_by_query(query):
    api_url = f"https://puyodb-api-deno.herokuapp.com/api/v1/characters/{query}"
    querystring = {'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_character_by_query('ekoro')

