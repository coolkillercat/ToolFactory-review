import requests
                
def authentication():
    api_url = f"missing"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
authentication()

import requests
                
def paginated_data_retrieval(page, page_size):
    api_url = f"missing"
    querystring = {'page': 1, 'page_size': 20, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
paginated_data_retrieval(1, 20)

