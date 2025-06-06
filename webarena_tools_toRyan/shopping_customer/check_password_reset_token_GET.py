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

def check_password_reset_token(customerId=None, resetPasswordLinkToken=None):
    """
    Check if password reset token is valid.
    
    Args:
        customerId (int): The customer ID. Example: 123
        resetPasswordLinkToken (str): The reset password link token. Example: 'abc123token'
        
    Returns:
        requests.Response: The API response
    """
    assert customerId is not None, 'Missing required parameter: customerId'
    assert resetPasswordLinkToken is not None, 'Missing required parameter: resetPasswordLinkToken'
    
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/customers/{quote(str(customerId), safe='')}/password/resetLinkToken/{quote(str(resetPasswordLinkToken), safe='')}"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_shopping_customer_auth_token(),
    }
    
    response = requests.get(url=api_url, headers=headers, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response

if __name__ == '__main__':
    r = check_password_reset_token(customerId=123, resetPasswordLinkToken='abc123token')
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