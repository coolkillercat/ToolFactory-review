import requests
                
def standard_language_detection(access_key, query):
    api_url = f"https://apilayer.net/api/detect"
    querystring = {'access_key': access_key, 'query': query, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
standard_language_detection('YOUR_ACCESS_KEY', 'Hello+World')

import requests
                
def batch_language_detection(access_key, query__):
    api_url = f"https://apilayer.net/api/batch"
    querystring = {'access_key': access_key, 'query__': query__, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
batch_language_detection('YOUR_ACCESS_KEY', ['Hello+World', 'Hola+Mundo', 'Hallo+Welt'])

