import requests
                
def get_mount_by_id(id):
    api_url = f"https://ffxivcollect.com/api/mounts/{id}"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_mount_by_id(186)

