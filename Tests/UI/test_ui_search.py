from playwright.sync_api import Page, expect
from Tests.UI.test_helpers.Pages.Login_Page import LoginPage
from Tests.UI.test_helpers.Pages.Book_Page import BookPage
from Tests.UI.test_helpers.Pages.Profile_Page import ProfilePage
from Tests.UI.test_helpers.Pages.Bookstore_Page import BookstorePage
from Tests.UI.test_helpers import Booklist_functions


def test_search_in_profile(page: Page):
    profile_page = ProfilePage(page)

    # handled by fixture:
    # user exists
    # user logged in
    # user has four books
    # yield

    # profile page open
    # search for one digit, than another
    # check booklist changes
    # assert search has result


def test_search_in_bookstore(page: Page):
    bookstore_page = BookstorePage(page)

    # handled by fixture:
    # user exists
    # user logged in
    # got to bookstore
    # yield

    # bookstore page open
    # search
    # assert search has result


def test_search_in_profile_empty(page: Page):
    profile_page = ProfilePage(page)




def test_search_in_bookstore_no_match(page: Page):
    bookstore_page = BookstorePage(page)


