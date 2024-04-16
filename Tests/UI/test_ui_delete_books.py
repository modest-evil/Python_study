from playwright.sync_api import Page
from Tests.UI.test_helpers.Pages.Login_Page import LoginPage
from Tests.UI.test_helpers.Pages.Book_Page import BookPage
from Tests.UI.test_helpers.Pages.Profile_Page import ProfilePage
from Tests.UI.test_helpers.Pages.Bookstore_Page import BookstorePage
from Tests.UI.test_helpers import Booklist_functions

from Tests.UI.test_fixtures.ui_fixtures import before_test
from Tests.UI.test_fixtures.ui_fixtures import user_exists_has_books

from dotenv import load_dotenv
import os

load_dotenv()
name = os.getenv("UI_TEST_USER")
password = os.getenv("UI_TEST_PASS")

def test_delete_book_raw(page: Page):
    #login
    page.goto("https://demoqa.com/login")
    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill("Anne")
    page.get_by_placeholder("UserName").press("Tab")
    page.get_by_placeholder("Password").fill("Anne123!")
    page.get_by_role("button", name="Login").click()

    #add one book
    page.get_by_role("button", name="Go To Book Store").click()
    page.get_by_role("link", name="Git Pocket Guide").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add To Your Collection").click()
    page.get_by_role("button", name="Back To Book Store").click()

    #add one more book
    page.get_by_role("link", name="Learning JavaScript Design").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add To Your Collection").click()
    page.get_by_role("button", name="Back To Book Store").click()

    #delete book
    page.get_by_text("Profile").click()
    page.get_by_role("row", name="image Git Pocket Guide").locator("path").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="OK").click()

    #check you have no deleted book


def test_delete_all_books_raw(page: Page):
    #login
    page.goto("https://demoqa.com/login")
    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill("Anne")
    page.get_by_placeholder("UserName").press("Tab")
    page.get_by_placeholder("Password").fill("Anne123!")
    page.get_by_role("button", name="Login").click()

    #add book
    page.get_by_role("button", name="Go To Book Store").click()
    page.get_by_role("link", name="Git Pocket Guide").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add To Your Collection").click()
    page.get_by_role("button", name="Back To Book Store").click()

    #add one more book
    page.get_by_role("link", name="Learning JavaScript Design").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add To Your Collection").click()
    page.get_by_role("button", name="Back To Book Store").click()

    #delete all books
    page.get_by_text("Profile").click()
    page.get_by_role("button", name="Delete All Books").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="OK").click()

    #check there is no books


def test_delete_one_book(user_exists_has_books):

    profile_page = ProfilePage(user_exists_has_books)
    profile_page.open()

    # count user books
    # delete one book from shelf
    # assert user have two books

    booklist_before = profile_page.get_user_books()
    book_amount = len(booklist_before)
    bookName = booklist_before.pop(1)

    profile_page.delete_book(bookName)

    booklist_after = profile_page.get_user_books()

    assert book_amount - len(booklist_after) == 1



def test_delete_all_books(user_exists_has_books):

    profile_page = ProfilePage(user_exists_has_books)
    profile_page.open()

    profile_page.delete_all_books()

    # count user books
    # delete all
    # assert user's booklist is empty

    booklist = profile_page.get_user_books()

    assert len(booklist) == 0
