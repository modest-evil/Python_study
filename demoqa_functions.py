import requests
import json


def extract_key_value(json_data, key):
    """Extracts a specific key-value pair from a JSON data"""
    data = json.loads(json_data)
    value = data.get(key)
    return value


def create_user():
    url = "https://demoqa.com/Account/v1/User"

    payload = json.dumps({
        "userName": "Dori",
        "password": "Dori123!"})

    headers = {
        'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    print(response.json)

