import requests
                
def fetch_news_by_category(category):
    api_url = f"https://inshorts.deta.dev/news?category={category_name}"
    querystring = {'category': category, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_news_by_category('science')

