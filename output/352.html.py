import requests
                
def create_custom_qr_code(data):
    api_url = f"/qr/custom"
    payload = {'data': data, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_custom_qr_code('https://www.example.com')

import requests
                
def create_transparent_qr_code(data):
    api_url = f"/qr/transparent"
    payload = {'data': data, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_transparent_qr_code('https://www.example.com')

import requests
                
def upload_image(file):
    api_url = f"/qr/uploadImage"
    payload = {'file': file, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
upload_image(example.png)

