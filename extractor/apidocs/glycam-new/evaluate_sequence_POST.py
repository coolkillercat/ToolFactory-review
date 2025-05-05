import requests
from urllib.parse import quote
                
def evaluate_sequence(sequence=None):
    api_url = f"https://glycam.org/json/evaluate_sequence"
    payload = {'sequence': sequence, }
    assert sequence is not None, 'Missing required parameter: sequence'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = evaluate_sequence(sequence='''DManpa1-6DManpa1-OH''')
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

