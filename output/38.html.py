import requests
                
def search_makeup_products():
    api_url = f"http://makeup-api.herokuapp.com/api/v1/products.json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_makeup_products()

