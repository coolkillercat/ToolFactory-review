import requests
                
def show_the_current_service_and_user():
    api_url = f"https://connect.ifttt.com/v2/me"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
show_the_current_service_and_user()

import requests
                
def show_a_connection(connection_id):
    api_url = f"https://connect.ifttt.com/v2/connections/{{connection_id}}"
    querystring = {'connection_id': connection_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
show_a_connection('C8p3q9T6')

import requests
                
def field_options(connection_id, type, type_id):
    api_url = f"https://connect.ifttt.com/v2/connections/{{connection_id}}/{{type}}/{{type_id}}/field_options"
    querystring = {'connection_id': connection_id, 'type': type, 'type_id': type_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
field_options('C8p3q9T6', 'actions', 'acme_cloud_storage.archive')

import requests
                
def refresh_a_connection(connection_id, user_id):
    api_url = f"https://connect.ifttt.com/v2/connections/{{connection_id}}/user_connection/refresh"
    payload = {'connection_id': connection_id, 'user_id': user_id, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
refresh_a_connection('C8p3q9T6', '123')

import requests
                
def connection_enabled_webhook():
    api_url = f"missing"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
connection_enabled_webhook()

import requests
                
def connection_updated_webhook():
    api_url = f"missing"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
connection_updated_webhook()

import requests
                
def connection_disabled_webhook():
    api_url = f"missing"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
connection_disabled_webhook()

import requests
                
def trigger_event_webhook():
    api_url = f"missing"
    payload = {}
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
trigger_event_webhook()

import requests
                
def test_trigger_event_webhook(connection_id, trigger_id, user_id):
    api_url = f"https://connect.ifttt.com/v2/connections/{{connection_id}}/triggers/{{trigger_id}}/test"
    payload = {'connection_id': connection_id, 'trigger_id': trigger_id, 'user_id': user_id, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
test_trigger_event_webhook('C8p3q9T6', 'acme_cloud_storage.new_file_added', '123')

import requests
                
def perform_a_query(connection_id, query_id, user_id):
    api_url = f"https://connect.ifttt.com/v2/connections/{{connection_id}}/queries/{{query_id}}/perform"
    payload = {'connection_id': connection_id, 'query_id': query_id, 'user_id': user_id, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
perform_a_query('C8p3q9T6', 'acme_cloud_storage.list_files', '123')

import requests
                
def run_an_action(connection_id, action_id, user_id):
    api_url = f"https://connect.ifttt.com/v2/connections/{{connection_id}}/actions/{{action_id}}/run"
    payload = {'connection_id': connection_id, 'action_id': action_id, 'user_id': user_id, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
run_an_action('C8p3q9T6', 'acme_cloud_storage.upload_from_url', '123')

