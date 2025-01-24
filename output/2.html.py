import requests
                
def shorten_long_urls(url):
    api_url = f"https://spoo.me/"
    payload = {'url': url, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
shorten_long_urls('https://example.com')

import requests
                
def shorten_urls_with_emojis(url):
    api_url = f"https://spoo.me/emoji/"
    payload = {'url': url, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
shorten_urls_with_emojis('https://example.com')

import requests
                
def url_statistics(shortCode):
    api_url = f"https://spoo.me/stats/{shortCode}"
    payload = {'shortCode': shortCode, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
url_statistics('exa')

import requests
                
def export_data(shortCode, exportFormat):
    api_url = f"https://spoo.me/export/{shortCode}/{exportFormat}"
    payload = {'shortCode': shortCode, 'exportFormat': exportFormat, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
export_data('exa', 'xlsx')

