import requests
                
def get_user_presence_data(user_id):
    api_url = f"https://api.lanyard.rest/v1/users/:user_id"
    querystring = {'user_id': user_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_user_presence_data('94490510688792576')

