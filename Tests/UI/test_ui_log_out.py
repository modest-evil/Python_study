from playwright.sync_api import Page, expect
from Tests.UI.test_helpers.Pages.Login_Page import LoginPage
from Tests.UI.test_helpers.Pages.Book_Page import BookPage
from Tests.UI.test_helpers.Pages.Profile_Page import ProfilePage
from Tests.UI.test_helpers.Pages.Bookstore_Page import BookstorePage
from Tests.UI.test_helpers import Booklist_functions

from Tests.UI.test_fixtures.ui_fixtures import before_test
from Tests.UI.test_fixtures.ui_fixtures import user_logged_in

from dotenv import load_dotenv
import os

load_dotenv()
test_username = os.getenv("TESTUSER")
test_password = os.getenv("PASSWORD")
start_page = os.getenv("LOGIN_PAGE_URL")


def test_logout_from_profile(user_logged_in):
    profile_page = ProfilePage(user_logged_in)
    profile_page.open()
    profile_page.log_out()

    expect(user_logged_in).to_have_url(start_page)


def test_logout_from_bookstore(user_logged_in):
    bookstore_page = BookstorePage(user_logged_in)
    bookstore_page.open()
    bookstore_page.log_out()

    expect(user_logged_in).to_have_url(start_page)


def test_logout_from_bookpage(user_logged_in):
    book_page = BookPage(user_logged_in)

    # handled by fixture:
    # user exists
    # user logged in
    # yield

    # book page open
    # log out
    # assert page has login page url
