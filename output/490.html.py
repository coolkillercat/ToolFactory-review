import requests
                
def get_random_geek_joke():
    api_url = f"https://geek-jokes.sameerkumar.website/api?format=json"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_geek_joke()

