import requests
                
def get_post_office_s__details_by_postal_pin_code(PINCODE):
    api_url = f"https://api.postalpincode.in/pincode/{PINCODE}"
    querystring = {'PINCODE': PINCODE, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_post_office_s__details_by_postal_pin_code('110001')

import requests
                
def get_post_office_s__details_by_post_office_branch_name(POSTOFFICEBRANCHNAME):
    api_url = f"https://api.postalpincode.in/postoffice/{POSTOFFICEBRANCHNAME}"
    querystring = {'POSTOFFICEBRANCHNAME': POSTOFFICEBRANCHNAME, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_post_office_s__details_by_post_office_branch_name('New Delhi')

