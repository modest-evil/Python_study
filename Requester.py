import requests


class Requester:

    def post(self, url):
        response = requests.post(url)


    def put(self, url):
        response = requests.put(url)


    def delete(self, url):
        response = requests.delete(url)


    def get(self, url):
        response = requests.get(url)
