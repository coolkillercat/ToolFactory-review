import requests
                
def check_if_a_number_is_even(number):
    api_url = f"https://api.isevenapi.xyz/api/iseven/{number}/"
    querystring = {'number': number, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
check_if_a_number_is_even(6)

