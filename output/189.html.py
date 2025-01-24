import requests
                
def validate_phone_number(number):
    api_url = f"https://numvalidate.com/api/validate"
    querystring = {'number': number, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
validate_phone_number('12015550123')

