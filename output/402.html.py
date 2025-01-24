import requests
                
def generate_bacon_ipsum_text():
    api_url = f"https://baconipsum.com/api/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_bacon_ipsum_text()

