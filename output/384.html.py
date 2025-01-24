import requests
                
def full_height_capture(access_key, url):
    api_url = f"http://api.screenshotlayer.com/api/capture"
    querystring = {'access_key': access_key, 'url': url, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
full_height_capture('YOUR_ACCESS_KEY', 'http://facebook.com')

import requests
                
def thumbnail_capture(access_key, url):
    api_url = f"http://api.screenshotlayer.com/api/capture"
    querystring = {'access_key': access_key, 'url': url, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
thumbnail_capture('YOUR_ACCESS_KEY', 'http://amazon.com')

import requests
                
def http_headers_capture(access_key, url):
    api_url = f"http://api.screenshotlayer.com/api/capture"
    querystring = {'access_key': access_key, 'url': url, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
http_headers_capture('YOUR_ACCESS_KEY', 'http://tumblr.com')

