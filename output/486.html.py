import requests
                
def get_bear_image(width, height):
    api_url = f"https://placebear.com/{width}/{height}"
    querystring = {'width': width, 'height': height, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_bear_image(200, 300)

