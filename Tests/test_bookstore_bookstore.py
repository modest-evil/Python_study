import json
import requests
import user_funcs
import bookstore_funcs


#Why it can not parse string? Need to be able retrieve list of isbn's from responce
def test_get_books():
    show = bookstore_funcs.Bookstore("https://demoqa.com")

    #print(show.get_books())

    temp = show.get_books()
    status = temp["status"]

    assert status == 200


# take isbn from list of isbn's; check isbn of added book in user's list
def test_add_book():
    user = user_funcs.User("https://demoqa.com")
    show = bookstore_funcs.Bookstore("https://demoqa.com")

    temp = json.loads(str(user.create_user("Fido", "Fido123!")).replace("'", '"'))
    result = json.loads(str(temp["body"]).replace("'", '"'))
    userId = result["userID"]

    temp = json.loads(str(user.log_in("Fido", "Fido123!")).replace("'", '"'))
    result = json.loads(str(temp["body"]).replace("'", '"'))
    sessionToken = result["token"]

   # print(show.add_books(userId, sessionToken, "9781449325862"))

    temp = json.loads(str(show.add_books(userId, sessionToken, "9781449325862")).replace("'", '"'))
    status = temp["status"]

    assert status == 201

#take isbn from list of isbn's; check user has no books
def test_delete_user_books():
    user = user_funcs.User("https://demoqa.com")
    show = bookstore_funcs.Bookstore("https://demoqa.com")

    temp = json.loads(str(user.create_user("Gary", "Gary123!")).replace("'", '"'))
    result = json.loads(str(temp["body"]).replace("'", '"'))
    userId = result["userID"]

    temp = json.loads(str(user.log_in("Gary", "Gary123!")).replace("'", '"'))
    result = json.loads(str(temp["body"]).replace("'", '"'))
    sessionToken = result["token"]

    show.add_books(userId, sessionToken, "9781449325862")
    show.add_books(userId, sessionToken, "9781449331818")

    status = show.delete_user_books(userId, sessionToken)

    assert status == 204

# check that user's book list does not contain isbn of removed book
def test_delete_one_book():
    user = user_funcs.User("https://demoqa.com")
    show = bookstore_funcs.Bookstore("https://demoqa.com")

    temp = json.loads(str(user.create_user("Homa", "Homa123!")).replace("'", '"'))
    result = json.loads(str(temp["body"]).replace("'", '"'))
    userId = result["userID"]

    temp = json.loads(str(user.log_in("Homa", "Homa123!")).replace("'", '"'))
    result = json.loads(str(temp["body"]).replace("'", '"'))
    sessionToken = result["token"]

    show.add_books(userId, sessionToken, "9781449325862")
    show.add_books(userId, sessionToken, "9781449331818")

    status = show.delete_one_book(userId, sessionToken, "9781449331818")

    assert status == 204


def test_change_isbn():
    user = user_funcs.User("https://demoqa.com")
    show = bookstore_funcs.Bookstore("https://demoqa.com")

    temp = json.loads(str(user.create_user("Iren", "Iren123!")).replace("'", '"'))
    result = json.loads(str(temp["body"]).replace("'", '"'))
    userId = result["userID"]

    temp = json.loads(str(user.log_in("Iren", "Iren123!")).replace("'", '"'))
    result = json.loads(str(temp["body"]).replace("'", '"'))
    sessionToken = result["token"]

    show.add_books(userId, sessionToken, "9781449325862")
    show.add_books(userId, sessionToken, "9781449331818")

   # print(show.change_isbn("9781449325862", "9781449337711", userId, sessionToken))

    temp = json.loads(str(show.change_isbn("9781449325862", "9781449337711", userId, sessionToken)).replace("'", '"'))
    status = temp["status"]

    assert status == 200

