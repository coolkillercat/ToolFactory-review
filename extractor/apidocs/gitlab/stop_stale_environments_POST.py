import requests, json
from urllib.parse import quote


def stop_stale_environments(id=None, before=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023/api/v4/projects/:id/environments/stop_stale"
    payload = {'id': id, 'before': before, }
    headers = {
        "Authorization": "Bearer " + "glpat-XzuH4hDT8YsJtYY3HMcE",
        "PRIVATE-TOKEN": "glpat-XzuH4hDT8YsJtYY3HMcE",
        "Private-Token": "glpat-XzuH4hDT8YsJtYY3HMcE",
    }
    assert id is not None, 'Missing required parameter: id'
    assert before is not None, 'Missing required parameter: before'
    
    response = requests.post(url=api_url, headers=headers, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = stop_stale_environments(id=1, before=2023-09-01T00:00:00Z)
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

