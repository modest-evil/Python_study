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

def test_add_book_codegen(page: Page):
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

    #go to profile check you have books
    page.locator("li").filter(has_text="Profile").click()


def test_add_book(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.log_in(name, password)

    profile_page = ProfilePage(page)
    profile_page.go_to_bookstore()

    bookstore_page = BookstorePage(page)
    Books = Booklist_functions.get_booklist(page)
    assert len(Books) > 0
    book_1 = Books.pop(0)
#    book_2 = Books.pop(2)
    bookstore_page.select_book(book_1)

    book_page = BookPage(page)
    book_page.add_book()
    book_page.back_to_bookstore()
#    bookstore_page.add_book(book_2)

    profile_page.open()
    user_books = Booklist_functions.get_booklist(page)

    assert len(user_books) == 1

