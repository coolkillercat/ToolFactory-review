import requests
                
def basic_call(img):
    api_url = f"http://api.resmush.it/ws.php"
    querystring = {'img': img, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
basic_call('https://resmush.it/wp-content/uploads/2024/02/testimage.jpg')

import requests
                
def basic_call_with_post(img):
    api_url = f"http://api.resmush.it/ws.php"
    payload = {'img': img, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
basic_call_with_post('https://resmush.it/wp-content/uploads/2024/02/testimage.jpg')

import requests
                
def basic_call_with_files(files):
    api_url = f"http://api.resmush.it/ws.php"
    payload = {'files': files, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
basic_call_with_files(/path/to/myfile.jpg)

