import json
import requests
from user_funcs import User
from bookstore_funcs import Bookstore


#Why it can not parse string? Need to be able retrieve list of isbn's from responce
def test_get_books():
    show = Bookstore("https://demoqa.com")

    temp = show.get_books()
    status = temp["status"]

    assert status == 200


# take isbn from list of isbn's; check isbn of added book in user's list
def test_add_book():
    user = User("https://demoqa.com")
    show = Bookstore("https://demoqa.com")

    user.create_user("Fido", "Fido123!")
    user.log_in("Fido", "Fido123!")

    #temp = show.add_books(user.userId, user.sessionToken, "9781449325862")
    isbns = show.get_booklist()
    isbn = isbns.pop(0)
    temp = show.add_books(user.userId, user.sessionToken, isbn)
    status = temp["status"]

    assert status == 201

#take isbn from list of isbn's; check user has no books
def test_delete_user_books():
    user = User("https://demoqa.com")
    show = Bookstore("https://demoqa.com")

    user.create_user("Gary", "Gary123!")
    user.log_in("Gary", "Gary123!")

    isbns = show.get_booklist()
    isbn_1 = isbns.pop(0)
    isbn_2 = isbns.pop(1)

    # show.add_books(user.userId, user.sessionToken, "9781449325862")
    # show.add_books(user.userId, user.sessionToken, "9781449331818")

    show.add_books(user.userId, user.sessionToken, isbn_1)
    show.add_books(user.userId, user.sessionToken, isbn_2)

    status = show.delete_user_books(user.userId, user.sessionToken)

    assert status == 204

# check that user's book list does not contain isbn of removed book
def test_delete_one_book():
    user = User("https://demoqa.com")
    show = Bookstore("https://demoqa.com")

    user.create_user("Homa", "Homa123!")
    user.log_in("Homa", "Homa123!")

    isbns = show.get_booklist()
    isbn_1 = isbns.pop(0)
    isbn_2 = isbns.pop(1)

    show.add_books(user.userId, user.sessionToken, isbn_1)
    show.add_books(user.userId, user.sessionToken, isbn_2)

    status = show.delete_one_book(user.userId, user.sessionToken, isbn_1)

    assert status == 204


def test_change_isbn():
    user = User("https://demoqa.com")
    show = Bookstore("https://demoqa.com")

    user.create_user("Iren", "Iren123!")
    user.log_in("Iren", "Iren123!")

    isbns = show.get_booklist()
    isbn_1 = isbns.pop(0)
    isbn_2 = isbns.pop(1)
    isbn_3 = isbns.pop(2)

    show.add_books(user.userId, user.sessionToken, isbn_1)
    show.add_books(user.userId, user.sessionToken, isbn_2)

    temp = show.change_isbn(isbn_1, isbn_3, user.userId, user.sessionToken)
    status = temp["status"]

    assert status == 200

