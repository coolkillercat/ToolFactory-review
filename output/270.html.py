import requests
                
def detect_browser__os__and_device_from_user_agent__get_(user_agent):
    api_url = f"https://api.apicagent.com"
    querystring = {'user_agent': user_agent, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
detect_browser__os__and_device_from_user_agent__get_('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

import requests
                
def detect_browser__os__and_device_from_user_agent__post_(user_agent):
    api_url = f"https://api.apicagent.com"
    payload = {'user_agent': user_agent, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
detect_browser__os__and_device_from_user_agent__post_('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

