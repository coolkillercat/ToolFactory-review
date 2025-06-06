import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    response = requests.post(
        url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

def check_email_availability(customerEmail=None, websiteId=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/customers/isEmailAvailable"
    payload = {'customerEmail': customerEmail, 'websiteId': websiteId, }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    assert customerEmail is not None, 'Missing required parameter: customerEmail'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = check_email_availability(customerEmail='''example@example.com''', websiteId=1)
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))

