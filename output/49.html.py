import requests
                
def get_quote(method, format):
    api_url = f"http://api.forismatic.com/api/1.0/"
    querystring = {'method': 'getQuote', 'format': format, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_quote('getQuote', 'json')

