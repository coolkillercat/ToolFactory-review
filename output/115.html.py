import requests
                
def datastore_search(resource_id):
    api_url = f"http://185.53.98.141/api/action/datastore_search?resource_id={ID_ZASOBU}"
    querystring = {'resource_id': resource_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
datastore_search('ff6e5973-32d5-4a64-b499-8ce65abb73fb')

