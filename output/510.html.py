import requests
                
def validate_single_email(email):
    api_url = f"https://www.disify.com/api/email/your@example.com"
    querystring = {'email': email, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
validate_single_email('your@example.com')

import requests
                
def validate_mass_emails(emails):
    api_url = f"https://www.disify.com/api/email/your@example.com,another@mail.com/mass"
    querystring = {'emails': emails, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
validate_mass_emails('your@example.com,another@mail.com')

import requests
                
def validate_mass_domains(domains):
    api_url = f"https://www.disify.com/api/domain/yourdomain.com,anotherdomain.com/mass"
    querystring = {'domains': domains, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
validate_mass_domains('yourdomain.com,anotherdomain.com')

import requests
                
def view_valid_results(session):
    api_url = f"https://www.disify.com/api/view/d117271ce938bf91bc718f6cfb7954de"
    querystring = {'session': session, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
view_valid_results('d117271ce938bf91bc718f6cfb7954de')

