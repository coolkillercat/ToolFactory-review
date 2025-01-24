import requests
                
def block_temporary_emails(email):
    api_url = f"missing"
    querystring = {'email': email, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
block_temporary_emails('example@mailinator.com')

