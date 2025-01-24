import requests
                
def get_json_response():
    api_url = f"http://itsthisforthat.com/api.php?json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_json_response()

import requests
                
def get_jsonp_response(call):
    api_url = f"http://itsthisforthat.com/api.php?call=myfunc"
    querystring = {'call': call, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_jsonp_response('myfunc')

import requests
                
def get_text_response():
    api_url = f"http://itsthisforthat.com/api.php?text"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_text_response()

