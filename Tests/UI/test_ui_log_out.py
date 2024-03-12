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


def test_logout_from_profile(user_logged_in, page: Page):

    profile_page = ProfilePage(page)
    profile_page.open()
    profile_page.log_out()

    expect(page).to_have_url(start_page)

    # handled by fixture:
    # user exists
    # user logged in
    # yield

    # profile page open
    # log out
    # assert page has login page url


def test_logout_from_bookstore(user_logged_in, page: Page):
    bookstore_page = BookstorePage(page)
    bookstore_page.open()
    bookstore_page.log_out()

    expect(page).to_have_url(start_page)

    # handled by fixture:
    # user exists
    # user logged in
    # yield

    # bookstore page open
    # log out
    # assert page has login page url


def test_logout_from_bookpage(page: Page):
    book_page = BookPage(page)

    # handled by fixture:
    # user exists
    # user logged in
    # yield

    # book page open
    # log out
    # assert page has login page url
