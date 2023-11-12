import requests
import json


def test_create_account():
    url = "https://demoqa.com/Account/v1/User"

    payload = json.dumps({
        "userName": "Dori",
        "password": "Dori123!"})

    headers = {
        'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def test_log_in():
    url = "https://demoqa.com/Account/v1/GenerateToken"

    payload = json.dumps({
        "userName": "Dori",
        "password": "Dori123!"})

    headers = {
        'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def test_is_logged_in():
    url = "https://demoqa.com/Account/v1/Authorized"

    payload = json.dumps({
        "userName": "Evan",
        "password": "Evan123!"})

    headers = {
        'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
