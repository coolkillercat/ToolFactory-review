import requests
                
def generate_placeholder_text():
    api_url = f"https://loripsum.net/api"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_placeholder_text()

