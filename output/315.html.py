import requests
                
def get_package_info(package):
    api_url = f"https://data.jsdelivr.com/v1/package/npm/:package"
    querystring = {'package': package, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_package_info('react')

import requests
                
def get_package_version_info(package, version):
    api_url = f"https://data.jsdelivr.com/v1/package/npm/:package@:version"
    querystring = {'package': package, 'version': version, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_package_version_info('react', '16.13.1')

import requests
                
def get_package_file_info(package, version, file):
    api_url = f"https://data.jsdelivr.com/v1/package/npm/:package@:version/file/:file"
    querystring = {'package': package, 'version': version, 'file': file, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_package_file_info('react', '16.13.1', 'umd/react.production.min.js')

