import requests
                
def get_status_code_image(format, status_code):
    api_url = f"https://vadivelu.anoram.com/[format]/[status_code]"
    querystring = {'format': format, 'status_code': status_code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_status_code_image('gif', 200)

