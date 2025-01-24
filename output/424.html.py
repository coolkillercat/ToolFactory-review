import requests
                
def get_email_address(f, ip, agent):
    api_url = f"http://api.guerrillamail.com/ajax.php"
    querystring = {'f': f, 'ip': ip, 'agent': agent, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_email_address('get_email_address', '127.0.0.1', 'Mozilla/5.0')

import requests
                
def set_email_user(f, ip, agent, email_user):
    api_url = f"http://api.guerrillamail.com/ajax.php"
    payload = {'f': f, 'ip': ip, 'agent': agent, 'email_user': email_user, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
set_email_user('set_email_user', '127.0.0.1', 'Mozilla/5.0', 'test')

import requests
                
def check_email(f, ip, agent, seq):
    api_url = f"http://api.guerrillamail.com/ajax.php"
    querystring = {'f': f, 'ip': ip, 'agent': agent, 'seq': seq, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
check_email('check_email', '127.0.0.1', 'Mozilla/5.0', 1)

import requests
                
def get_email_list(f, ip, agent, offset):
    api_url = f"http://api.guerrillamail.com/ajax.php"
    querystring = {'f': f, 'ip': ip, 'agent': agent, 'offset': offset, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_email_list('get_email_list', '127.0.0.1', 'Mozilla/5.0', 0)

import requests
                
def fetch_email(f, ip, agent, email_id):
    api_url = f"http://api.guerrillamail.com/ajax.php"
    querystring = {'f': f, 'ip': ip, 'agent': agent, 'email_id': email_id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
fetch_email('fetch_email', '127.0.0.1', 'Mozilla/5.0', 123)

import requests
                
def forget_me(f, ip, agent, email_addr):
    api_url = f"http://api.guerrillamail.com/ajax.php"
    payload = {'f': f, 'ip': ip, 'agent': agent, 'email_addr': email_addr, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
forget_me('forget_me', '127.0.0.1', 'Mozilla/5.0', 'test@guerrillamailblock.com')

import requests
                
def delete_email(f, ip, agent, email_ids):
    api_url = f"http://api.guerrillamail.com/ajax.php"
    payload = {'f': f, 'ip': ip, 'agent': agent, 'email_ids': email_ids, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
delete_email('del_email', '127.0.0.1', 'Mozilla/5.0', [425, 426, 427])

import requests
                
def extend(f, ip, agent):
    api_url = f"http://api.guerrillamail.com/ajax.php"
    payload = {'f': f, 'ip': ip, 'agent': agent, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
extend('extend', '127.0.0.1', 'Mozilla/5.0')

