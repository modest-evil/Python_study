import json
import requests
from demoqa_functions import Demoqa

class Bookstore(Demoqa):

    def __init__(self, host):
        super().__init__(host)


    # def __init__(self, host):
    #     self.host = host

    def get_books(self):
        url = self.host + "/BookStore/v1/Books"

        payload = {}
        headers = {
            'Content-Type': 'application/json'
        }

        try:
            response = requests.request("GET", url, headers=headers, data=payload)

        except:
            print('Error json parsing')

        # get all values of key "firstName"
        # first_names = [employee["firstName"] for employee in parsed_data["employees"]]

        # self.booklist = [book["isbn"] for book in response.json()["books"]]
        # print(self.booklist)

        return {"status": response.status_code, "body": response.json()}

    def get_booklist(self):
        res = self.get_books()
        response = res["body"]

        booklist = [book["isbn"] for book in response["books"]]
        print(booklist)

        return booklist


    def add_books(self, userId, sessionId, isbn):
        url = self.host + "/BookStore/v1/Books"

        payload = json.dumps({
            "userId": userId,
            "collectionOfIsbns": [
            {
                "isbn": isbn
            }
            ]
        })

        headers = {
            'Content-Type': 'application/json',
            'Authorization': ('Bearer ' + sessionId)}

        response = requests.request("POST", url, headers=headers, data=payload)

        return {"status": response.status_code, "body": response.json()}


    def delete_user_books(self, userId, sessionId):
        url = self.host + "/BookStore/v1/Books?UserId=" + userId

        payload = {}

        headers = {
            'Content-Type': 'application/json',
            'Authorization': ('Bearer ' + sessionId)}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        #return {"status": response.status_code, "body": response.json()}

        return response.status_code


    def delete_one_book(self, userId, sessionId, isbn):
        url = self.host + "/BookStore/v1/Book"

        payload = json.dumps({
            "isbn": isbn,
            "userId": userId})

        headers = {
            'Content-Type': 'application/json',
            'Authorization': ('Bearer ' + sessionId)}

        response = requests.request("DELETE", url, headers=headers, data=payload)

       # return {"status": response.status_code, "body": response.json()}
        return response.status_code


    def change_isbn(self, oldBook, newBook, userId, sessionId):
        url = self.host + "/BookStore/v1/Books/" + oldBook

        payload = json.dumps({
            "userId": userId,
            "isbn": newBook})

        headers = {
            'Content-Type': 'application/json',
            'Authorization': ('Bearer ' + sessionId)}

        response = requests.request("PUT", url, headers=headers, data=payload)

        return {"status": response.status_code, "body": response.json()}

