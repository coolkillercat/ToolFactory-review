import requests, json
from urllib.parse import quote


def list_project_merge_request_label_events(id=None, merge_request_iid=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/projects/{quote(id, safe='')}/merge_requests/{quote(merge_request_iid, safe='')}/resource_label_events"
    querystring = {'id': id, 'merge_request_iid': merge_request_iid, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert merge_request_iid is not None, 'Missing required parameter: merge_request_iid'
    
    response = requests.get(url=api_url, headers=headers, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = list_project_merge_request_label_events(id=5, merge_request_iid=11)
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

