import requests
                
def get_item_details(itemId):
    api_url = f"https://xivapi.com/item/{itemId}"
    querystring = {'itemId': itemId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_item_details(1675)

