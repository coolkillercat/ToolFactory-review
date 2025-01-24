import requests
                
def get_random_quote():
    api_url = f"https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_quote()

