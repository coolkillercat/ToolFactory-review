import requests
                
def site_endpoint(url):
    api_url = f"https://api.websitecarbon.com/site?url={xxx}"
    querystring = {'url': url, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
site_endpoint('https://www.wholegraindigital.com/')

import requests
                
def data_endpoint(bytes, green):
    api_url = f"https://api.websitecarbon.com/data?bytes={0000000}&green={1/0}"
    querystring = {'bytes': bytes, 'green': green, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
data_endpoint(1000, 1)

