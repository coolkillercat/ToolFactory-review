import requests
                
def generate_chart(cht, chd, chs):
    api_url = f"https://image-charts.com/chart"
    querystring = {'cht': cht, 'chd': chd, 'chs': chs, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_chart('p3', 't:60,40', '700x100')

