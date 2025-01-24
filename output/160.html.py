import requests
                
def get_keanu_image(width):
    api_url = f"https://placekeanu.com/[width]/[height]*/[options]*"
    querystring = {'width': width, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_keanu_image(200)

