import requests
                
def upload_file(file):
    api_url = f"https://0x0.st"
    payload = {'file': file, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
upload_file(@yourfile.png)

import requests
                
def upload_remote_url(url):
    api_url = f"https://0x0.st"
    payload = {'url': url, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
upload_remote_url('http://example.com/image.jpg')

import requests
                
def delete_file(token, delete):
    api_url = f"https://0x0.st/abc.txt"
    payload = {'token': token, 'delete': delete, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
delete_file('token_here', '')

import requests
                
def change_expiration_date(token, expires):
    api_url = f"https://0x0.st/abc.txt"
    payload = {'token': token, 'expires': expires, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
change_expiration_date('token_here', 3)

