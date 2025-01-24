import requests
                
def convert_easting_and_northing_to_latitude_and_longitude(easting, northing):
    api_url = f"https://api.getthedata.com/bng2latlong/[easting]/[northing]"
    querystring = {'easting': easting, 'northing': northing, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
convert_easting_and_northing_to_latitude_and_longitude(529090, 179645)

