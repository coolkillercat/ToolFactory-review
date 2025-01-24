import requests
                
def get_postal_code_information(postal_code):
    api_url = f"https://postali.app/codigo-postal/{postal_code}.json"
    querystring = {'postal_code': postal_code, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_postal_code_information('65936')

