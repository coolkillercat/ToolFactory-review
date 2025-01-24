import requests
                
def get_random_food_dish():
    api_url = f"https://foodish-api.com/api/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_food_dish()

import requests
                
def get_random_picture_from_food_category(food):
    api_url = f"https://foodish-api.com/api/images/:food"
    querystring = {'food': food, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_random_picture_from_food_category('biryani')

