import requests


url = "https://api.covid19api.com/summary"

payload = {}
headers= {}

def get_data():

    response = requests.request("GET", url, headers=headers, data = payload)

    data_json = response.json()

    world_cases = data_json['Global']['TotalRecovered']

    print(f"Amount of covid cases: {world_cases}")

    return world_cases
