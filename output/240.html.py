import requests
                
def get_api_routes():
    api_url = f"https://api.opensensemap.org/"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_api_routes()

import requests
                
def get_statistics():
    api_url = f"https://api.opensensemap.org/stats"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_statistics()

import requests
                
def get_all_tags():
    api_url = f"https://api.opensensemap.org/tags"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_tags()

import requests
                
def calculate_idw():
    api_url = f"https://api.opensensemap.org/statistics/idw"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
calculate_idw()

import requests
                
def get_descriptive_statistics():
    api_url = f"https://api.opensensemap.org/statistics/descriptive"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_descriptive_statistics()

import requests
                
def get_boxes():
    api_url = f"https://api.opensensemap.org/boxes"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_boxes()

import requests
                
def get_data_for_multiple_boxes():
    api_url = f"https://api.opensensemap.org/boxes/data"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_data_for_multiple_boxes()

import requests
                
def get_data_by_tag():
    api_url = f"https://api.opensensemap.org/boxes/data/bytag"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_data_by_tag()

import requests
                
def get_box_by_id(boxId):
    api_url = f"https://api.opensensemap.org/boxes/:boxId"
    querystring = {'boxId': boxId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_box_by_id('12345')

import requests
                
def get_sensors_of_a_box(boxId):
    api_url = f"https://api.opensensemap.org/boxes/:boxId/sensors"
    querystring = {'boxId': boxId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_sensors_of_a_box('12345')

import requests
                
def get_sensor_data(boxId, sensorId):
    api_url = f"https://api.opensensemap.org/boxes/:boxId/sensors/:sensorId"
    querystring = {'boxId': boxId, 'sensorId': sensorId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_sensor_data('12345', '67890')

import requests
                
def get_sensor_data_by_id(boxId, sensorId):
    api_url = f"https://api.opensensemap.org/boxes/:boxId/data/:sensorId"
    querystring = {'boxId': boxId, 'sensorId': sensorId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_sensor_data_by_id('12345', '67890')

import requests
                
def get_box_locations(boxId):
    api_url = f"https://api.opensensemap.org/boxes/:boxId/locations"
    querystring = {'boxId': boxId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_box_locations('12345')

import requests
                
def post_data_for_multiple_boxes():
    api_url = f"https://api.opensensemap.org/boxes/data"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
post_data_for_multiple_boxes()

import requests
                
def post_data_for_a_box(boxId):
    api_url = f"https://api.opensensemap.org/boxes/:boxId/data"
    payload = {'boxId': boxId, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
post_data_for_a_box('12345')

import requests
                
def post_data_for_a_sensor(boxId, sensorId):
    api_url = f"https://api.opensensemap.org/boxes/:boxId/:sensorId"
    payload = {'boxId': boxId, 'sensorId': sensorId, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
post_data_for_a_sensor('12345', '67890')

import requests
                
def register_user():
    api_url = f"https://api.opensensemap.org/users/register"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
register_user()

import requests
                
def request_password_reset():
    api_url = f"https://api.opensensemap.org/users/request-password-reset"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
request_password_reset()

import requests
                
def reset_password():
    api_url = f"https://api.opensensemap.org/users/password-reset"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
reset_password()

import requests
                
def confirm_email():
    api_url = f"https://api.opensensemap.org/users/confirm-email"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
confirm_email()

import requests
                
def sign_in():
    api_url = f"https://api.opensensemap.org/users/sign-in"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
sign_in()

import requests
                
def refresh_authentication():
    api_url = f"https://api.opensensemap.org/users/refresh-auth"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
refresh_authentication()

import requests
                
def get_user_info():
    api_url = f"https://api.opensensemap.org/users/me"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_user_info()

import requests
                
def get_user_boxes():
    api_url = f"https://api.opensensemap.org/users/me/boxes"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_user_boxes()

import requests
                
def get_user_box_by_id(boxId):
    api_url = f"https://api.opensensemap.org/users/me/boxes/:boxId"
    querystring = {'boxId': boxId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_user_box_by_id('12345')

import requests
                
def get_box_script(boxId):
    api_url = f"https://api.opensensemap.org/boxes/:boxId/script"
    querystring = {'boxId': boxId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_box_script('12345')

import requests
                
def post_new_box():
    api_url = f"https://api.opensensemap.org/boxes"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
post_new_box()

import requests
                
def claim_box():
    api_url = f"https://api.opensensemap.org/boxes/claim"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
claim_box()

import requests
                
def create_box_transfer():
    api_url = f"https://api.opensensemap.org/boxes/transfer"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_box_transfer()

import requests
                
def get_box_transfer_by_id(boxId):
    api_url = f"https://api.opensensemap.org/boxes/transfer/:boxId"
    querystring = {'boxId': boxId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_box_transfer_by_id('12345')

import requests
                
def sign_out():
    api_url = f"https://api.opensensemap.org/users/sign-out"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
sign_out()

import requests
                
def resend_email_confirmation():
    api_url = f"https://api.opensensemap.org/users/me/resend-email-confirmation"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
resend_email_confirmation()

