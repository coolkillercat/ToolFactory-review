import requests
                
def proxy_get_request():
    api_url = f"https://course-search-proxy.herokuapp.com"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
proxy_get_request()

