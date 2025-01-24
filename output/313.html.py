import requests
                
def content_object(post_title):
    api_url = f"https://www.healthcare.gov/:post-title.json"
    querystring = {'post_title': post_title, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
content_object('accessibility')

import requests
                
def content_collection(content_type):
    api_url = f"https://www.healthcare.gov/api/:content-type.json"
    querystring = {'content_type': content_type, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
content_collection('glossary')

import requests
                
def content_index():
    api_url = f"https://www.healthcare.gov/api/index.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
content_index()

