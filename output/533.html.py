import requests
                
def get_stoicism_quote():
    api_url = f"https://stoic.tekloon.net/stoic-quote"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_stoicism_quote()

