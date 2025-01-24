import requests
                
def get_thirukkural_poem(kural_num):
    api_url = f"https://api-thirukkural.vercel.app/api?num={kural_num}"
    querystring = {'kural_num': kural_num, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_thirukkural_poem(1)

