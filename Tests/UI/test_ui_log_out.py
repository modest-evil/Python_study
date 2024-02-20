from playwright.sync_api import Page, expect
from Tests.UI.test_helpers.Pages.Login_Page import LoginPage
from Tests.UI.test_helpers.Pages.Book_Page import BookPage
from Tests.UI.test_helpers.Pages.Profile_Page import ProfilePage
from Tests.UI.test_helpers.Pages.Bookstore_Page import BookstorePage
from Tests.UI.test_helpers import Booklist_functions

def test_logout_from_profile(page: Page):
    profile_page = ProfilePage(page)

    # handled by fixture:
    # user exists
    # user logged in
    # yield

    # profile page open
    # log out
    # assert page has login page url


def test_logout_from_bookstore(page: Page):
    bookstore_page = BookstorePage(page)

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
