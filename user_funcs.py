import json
import demoqa_functions
import requests


class User:
    userId = None
    sessionToken = None

    def __init__(self, host):
        self.host = host


    def create_user(self, userName, password):
        url = self.host + "/Account/v1/User"

        payload = json.dumps({
            "userName": userName,
            "password": password})

        headers = {
            'Content-Type': 'application/json'}

        response = requests.request("POST", url, headers=headers, data=payload)

        temp = json.loads(str(response.json()).replace("'", '"'))
        self.userId = temp["userID"]
        print(self.userId)

        return {"status": response.status_code, "body": temp}


    def log_in(self, userName, password):
        url = self.host + "/Account/v1/GenerateToken"

        payload = json.dumps({
            "userName": userName,
            "password": password})

        headers = {
            'Content-Type': 'application/json'}

        response = requests.request("POST", url, headers=headers, data=payload)

        temp = json.loads(str(response.json()).replace("'", '"'))
        self.sessionToken = temp["token"]
        print(self.sessionToken)

        return {"status": response.status_code, "body": response.json()}


    def is_logged_in(self, userName, password):
        url = self.host + "/Account/v1/Authorized"

        payload = json.dumps({
            "userName": userName,
            "password": password})

        headers = {
            'Content-Type': 'application/json'}

        response = requests.request("POST", url, headers=headers, data=payload)

        return {"status": response.status_code, "body": response.json()}


    def get_user_info(self, sessionId, userId):
        url = self.host + "/Account/v1/User/" + userId

        payload = {}

        headers = {
            'Content-Type': 'application/json',
            'Authorization': ('Bearer ' + sessionId)}

        response = requests.request("GET", url, headers=headers, data=payload)

        return {"status": response.status_code, "body": response.json()}


    def delete_account(self, sessionId, userId):
        url = self.host + "/Account/v1/User/" + userId
        print(url)

        payload = {}

        headers = {
            'Content-Type': 'application/json',
            'Authorization': ('Bearer ' + sessionId)}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        #return {"status": response.status_code, "body": response.json()}

        return response.status_code
