import requests
                
def create_assessment(deck_id):
    api_url = f"https://api.traitify.com/v1/assessments"
    payload = {'deck_id': deck_id, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_assessment('career-deck')

