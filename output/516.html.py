import requests
                
def generate_noise_background_image_with_rgb(r, g, b):
    api_url = f"https://php-noise.com/noise.php?r=${r}&g=${g}&b=${b}&tiles=${tiles}&tileSize=${tileSize}&borderWidth=${borderWidth}&mode=${mode}&json"
    querystring = {'r': r, 'g': g, 'b': b, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_noise_background_image_with_rgb(255, 255, 255)

import requests
                
def generate_noise_background_image_with_hex(hex):
    api_url = f"https://php-noise.com/noise.php?hex=${hex}&json"
    querystring = {'hex': hex, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_noise_background_image_with_hex('ff00ff')

import requests
                
def generate_noise_background_image_with_hex_and_base64(hex):
    api_url = f"https://php-noise.com/noise.php?hex=${hex}&json&base64"
    querystring = {'hex': hex, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
generate_noise_background_image_with_hex_and_base64('ff00ff')

import requests
                
def api_help():
    api_url = f"https://php-noise.com/noise.php?help"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
api_help()

