import requests
                
def search_cards(q):
    api_url = f"https://api.pokemontcg.io/v2/cards"
    querystring = {'q': q, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
search_cards('name:gardevoir (subtypes:mega OR subtypes:vmax)')

