import requests
                
def add_times(data):
    api_url = f"https://api-times-adder.up.railway.app/api/v1"
    payload = {'data': data, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
add_times(['4:20:01', '6:16', '69', 'x', 'y'])

