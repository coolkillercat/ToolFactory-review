import requests
                
def contains_profanity(text):
    api_url = f"https://www.purgomalum.com/service/containsprofanity"
    querystring = {'text': text, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
contains_profanity('this is some test input')

import requests
                
def xml_response(text):
    api_url = f"https://www.purgomalum.com/service/xml"
    querystring = {'text': text, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
xml_response('this is some test input')

import requests
                
def json_response(text):
    api_url = f"https://www.purgomalum.com/service/json"
    querystring = {'text': text, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
json_response('this is some test input')

import requests
                
def plain_text_response(text):
    api_url = f"https://www.purgomalum.com/service/plain"
    querystring = {'text': text, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
plain_text_response('this is some test input')

