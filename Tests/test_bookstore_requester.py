# import requests
# import json
# import demoqa_functions
# import user_funcs
#
#
# user = user_funcs.User("https://demoqa.com")
#
# def test_account_create_account():
#     url = "https://demoqa.com/Account/v1/User"
#
#     payload = json.dumps({
#         "userName": "Dori",
#         "password": "Dori123!"})
#
#     headers = {
#         'Content-Type': 'application/json'}
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     print(response.text)
#     print(response.json)
#     uid = demoqa_functions.extract_key_value(response.json, "userID")
#     print(uid)
#
#
# def test_account_log_in():
#     url = "https://demoqa.com/Account/v1/GenerateToken"
#
#     payload = json.dumps({
#         "userName": "Dori",
#         "password": "Dori123!"})
#
#     headers = {
#         'Content-Type': 'application/json'}
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     print(response.text)
#
#
# def test_account_is_logged_in():
#     url = "https://demoqa.com/Account/v1/Authorized"
#
#     payload = json.dumps({
#         "userName": "Evan",
#         "password": "Evan123!"})
#
#     headers = {
#         'Content-Type': 'application/json'}
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     print(response.text)
#
#
# def test_account_get_user_info():
#     url = "https://demoqa.com/Account/v1/User/36465101-8d23-46d5-923f-23df2d51add3"
#
#     payload = {}
#     headers = {
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IkV2YW4iLCJwYXNzd29yZCI6IkV2YW4xMjMhIiwiaWF0IjoxNjk5OTE3MDMxfQ.zbvXdWB9NAFD2T5br3ykJZOs5e8PeudEmMbWMvR6CnQ'}
#
#
#     response = requests.request("GET", url, headers=headers, data=payload)
#
#     print(response.text)
#
#
# def test_account_delete_user():
#     url = "https://demoqa.com/Account/v1/User/f7702308-486e-4cca-a504-ebcbe28451f3"
#
#     payload = {}
#     headers = {
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IkV2YW4iLCJwYXNzd29yZCI6IkV2YW4xMjMhIiwiaWF0IjoxNjk5OTk5NDY1fQ.mmgogszXG-ksrYg_6XKQu3Pgb3SDvpLP86lay6IKp6A'}
#
#     response = requests.request("DELETE", url, headers=headers, data=payload)
#
#     print(response.text)
#
#
# def test_bookstore_get_books():
#     url = "https://demoqa.com/BookStore/v1/Books"
#
#     payload = {}
#     headers = {}
#
#     response = requests.request("GET", url, headers=headers, data=payload)
#
#     print(response.text)
#
#
# def test_bookstore_change_isbn():
#     url = "https://demoqa.com/BookStore/v1/Books/9781449331818"
#
#     payload = json.dumps({
#         "userId": "7f02f157-f57b-427b-a7b6-a82cd2ce2dbc",
#         "isbn": "9781449331829"})
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IkV2YW4iLCJwYXNzd29yZCI6IkV2YW4xMjMhIiwiaWF0IjoxNzAwMDAxMTQ4fQ.q3MRkpCtL7G4MwxRevQnV7_DECvn_BaExRq_DYxormE'}
#
#     response = requests.request("PUT", url, headers=headers, data=payload)
#
#     print(response.text)
#
#
# def test_bookstore_add_books():
#     url = "https://demoqa.com/BookStore/v1/Books"
#
#     payload = json.dumps({
#         "userId": "7f02f157-f57b-427b-a7b6-a82cd2ce2dbc",
#         "collectionOfIsbns": [
#         {
#             "isbn": "9781449337711"
#         }
#         ]
#     })
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IkV2YW4iLCJwYXNzd29yZCI6IkV2YW4xMjMhIiwiaWF0IjoxNzAwMDAxMTQ4fQ.q3MRkpCtL7G4MwxRevQnV7_DECvn_BaExRq_DYxormE'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     print(response.text)
#
#
# def test_bookstore_delete_books():
#     url = "https://demoqa.com/BookStore/v1/Books/7f02f157-f57b-427b-a7b6-a82cd2ce2dbc"
#
#     payload = {}
#     headers = {
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IkV2YW4iLCJwYXNzd29yZCI6IkV2YW4xMjMhIiwiaWF0IjoxNzAwMDAxMTQ4fQ.q3MRkpCtL7G4MwxRevQnV7_DECvn_BaExRq_DYxormE'
#     }
#
#     response = requests.request("DELETE", url, headers=headers, data=payload)
#
#     print(response.text)
#
#
# def test_bookstore_delete_one_book():
#     url = "https://demoqa.com/BookStore/v1/Book"
#
#     payload = json.dumps({
#         "isbn": "9781449337711",
#         "userId": "7f02f157-f57b-427b-a7b6-a82cd2ce2dbc"})
#
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IkV2YW4iLCJwYXNzd29yZCI6IkV2YW4xMjMhIiwiaWF0IjoxNzAwMDAxMTQ4fQ.q3MRkpCtL7G4MwxRevQnV7_DECvn_BaExRq_DYxormE'}
#
#     response = requests.request("DELETE", url, headers=headers, data=payload)
#
#     print(response.text)
