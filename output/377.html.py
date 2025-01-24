import requests
                
def get_random_quote():
    api_url = f"https://strangerthings-quotes.vercel.app/api/quotes"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_quote()

import requests
                
def get_multiple_quotes(number):
    api_url = f"https://strangerthings-quotes.vercel.app/api/quotes/{number}"
    querystring = {'number': number, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_multiple_quotes(5)

