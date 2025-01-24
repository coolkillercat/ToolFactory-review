import requests
                
def generate_qr_code():
    api_url = f"https://qrtag.net/api/qr(_transparent)(_[size]).[png|svg](?url=[URL])"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_qr_code()

