import requests
                
def svátky_api():
    api_url = f"https://svatky.adresa.info/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
svátky_api()

