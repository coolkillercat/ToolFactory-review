import requests
                
def getbotid(username):
    api_url = f"/getBotID.php"
    querystring = {'username': username, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
getbotid('@vote')

import requests
                
def getuservote(user_id, bot_id):
    api_url = f"/getUserVote.php"
    querystring = {'user_id': user_id, 'bot_id': bot_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
getuservote('141691961', '1')

