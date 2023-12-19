from demoqa_fixtures import create_and_log_in
from demoqa_fixtures import cleanup

from user_funcs import User
from bookstore_funcs import Bookstore
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")

def test_get_books():
    show = Bookstore(url)
    assert show.get_books()["status"] == 200


def test_add_book(create_and_log_in):
    user = create_and_log_in
    show = Bookstore(url)

    isbns = show.get_booklist()
    isbn = isbns.pop(0)

    assert show.add_books(user.userId, user.sessionToken, isbn)["status"] == 201


def test_delete_user_books(create_and_log_in):
    user = create_and_log_in
    show = Bookstore(url)

    isbns = show.get_booklist()
    isbn_1 = isbns.pop(0)
    isbn_2 = isbns.pop(1)

    show.add_books(user.userId, user.sessionToken, isbn_1)
    show.add_books(user.userId, user.sessionToken, isbn_2)

    assert show.delete_user_books(user.userId, user.sessionToken) == 204


def test_delete_one_book(create_and_log_in):
    user = create_and_log_in
    show = Bookstore(url)

    isbns = show.get_booklist()
    isbn_1 = isbns.pop(0)
    isbn_2 = isbns.pop(1)

    show.add_books(user.userId, user.sessionToken, isbn_1)
    show.add_books(user.userId, user.sessionToken, isbn_2)

    assert show.delete_one_book(user.userId, user.sessionToken, isbn_1) == 204


def test_change_isbn(create_and_log_in):
    user = create_and_log_in
    show = Bookstore(url)

    isbns = show.get_booklist()
    isbn_1 = isbns.pop(0)
    isbn_2 = isbns.pop(1)
    isbn_3 = isbns.pop(2)

    show.add_books(user.userId, user.sessionToken, isbn_1)
    show.add_books(user.userId, user.sessionToken, isbn_2)

    assert show.change_isbn(isbn_1, isbn_3, user.userId, user.sessionToken)["status"] == 200

