from playwright.sync_api import Page
from Tests.UI.test_helpers.Pages.Login_Page import LoginPage
from Tests.UI.test_helpers.Pages.Book_Page import BookPage
from Tests.UI.test_helpers.Pages.Profile_Page import ProfilePage
from Tests.UI.test_helpers.Pages.Bookstore_Page import BookstorePage
from Tests.UI.test_helpers import Booklist_functions
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


def test_delete_one_book(page: Page):
    login_page = LoginPage(page)

    # handled by fixture

    # user exists
    # user logged in
    # user have three books on shelf
    # yield

    # count user books
    # delete one book from shelf
    # assert user have two books


def test_delete_all_books(page: Page):
    login_page = LoginPage(page)

    # handled by fixture

    # user exists
    # user logged in
    # user have three books on shelf
    # yield

    # count user books
    # delete all
    # assert user's booklist is empty
