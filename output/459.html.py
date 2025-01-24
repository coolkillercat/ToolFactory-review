import requests
                
def create_session_with_single_random_address(query):
    api_url = f"https://dropmail.me/api/graphql/${AUTH_TOKEN}"
    payload = {'query': query, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_session_with_single_random_address('mutation { introduceSession { id, expiresAt, addresses { address } } }')

import requests
                
def fetch_incoming_mail(query):
    api_url = f"https://dropmail.me/api/graphql/${AUTH_TOKEN}"
    payload = {'query': query, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_incoming_mail('query { session(id: "U2Vzc2lvbjqcMxamadJC_aLiPz_XL0lK") { mails { rawSize, fromAddr, toAddr, downloadUrl, text, headerSubject } } }')

import requests
                
def list_domains(query):
    api_url = f"https://dropmail.me/api/graphql/${AUTH_TOKEN}"
    payload = {'query': query, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
list_domains('query { domains { id, name, availableVia } }')

import requests
                
def add_address_to_session(query):
    api_url = f"https://dropmail.me/api/graphql/${AUTH_TOKEN}"
    payload = {'query': query, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
add_address_to_session('mutation { introduceAddress(input: {sessionId: "U2Vzc2lvbjqcMxamadJC_aLiPz_XL0lK"}) { address, restoreKey } }')

import requests
                
def subscribe_to_new_session_mail(query):
    api_url = f"wss://dropmail.me/api/graphql/${AUTH_TOKEN}/websocket"
    payload = {'query': query, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
subscribe_to_new_session_mail('subscription { sessionMailReceived(id: "U2Vzc2lvbjqcMxamadJC_aLiPz_XL0lK") { rawSize, fromAddr, toAddr, downloadUrl, text, headerSubject } }')

