import requests
                
def check_bank_card_bin_number(binNumber):
    api_url = f"missing"
    querystring = {'binNumber': binNumber, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
check_bank_card_bin_number('123456')

