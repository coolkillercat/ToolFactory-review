import requests
                
def request_colors_data(keyword, hex, rgb, rgba, hsl, hsla):
    api_url = f"https://color.serialif.com/"
    querystring = {'keyword': keyword, 'hex': hex, 'rgb': rgb, 'rgba': rgba, 'hsl': hsl, 'hsla': hsla, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
request_colors_data('aquamarine', '55667788', '85,102,119', '85,102,119,0.53', '85,102,119', '85,102,119,0.53')

