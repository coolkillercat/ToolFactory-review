import requests
                
def get_top_50_stocks_discussed_on_reddit_wallstreetbets():
    api_url = f"https://tradestie.com/api/v1/apps/reddit"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_top_50_stocks_discussed_on_reddit_wallstreetbets()

