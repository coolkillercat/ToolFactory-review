import requests
                
def generate_random_strings():
    api_url = f"https://ciprand.p3p.repl.co/api"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_random_strings()

