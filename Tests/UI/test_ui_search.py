from playwright.sync_api import Page, expect
from Tests.UI.test_helpers.Pages.Login_Page import LoginPage
from Tests.UI.test_helpers.Pages.Book_Page import BookPage
from Tests.UI.test_helpers.Pages.Profile_Page import ProfilePage
from Tests.UI.test_helpers.Pages.Bookstore_Page import BookstorePage
from Tests.UI.test_helpers import Booklist_functions

from Tests.UI.test_fixtures.ui_fixtures import before_test
from Tests.UI.test_fixtures.ui_fixtures import user_exists_has_books


def test_search_in_profile(user_exists_has_books):
    profile_page = ProfilePage(user_exists_has_books)
    profile_page.open()

    booklist_before = profile_page.get_user_books()
    found = booklist_before[0]

    profile_page.search(found)

    booklist_after = profile_page.get_user_books()

    assert found in booklist_after



def test_search_in_bookstore(page: Page):
    bookstore_page = BookstorePage(page)
    bookstore_page.open()

    booklist_before = bookstore_page.get_books()
    found = "Learning Java"

    bookstore_page.search(found)

    booklist_after = bookstore_page.get_books()

    assert len(booklist_before) > len(booklist_after)
    assert len(booklist_after) > 0


def test_search_in_profile_empty(page: Page):
    profile_page = ProfilePage(page)




def test_search_in_bookstore_no_match(page: Page):
    bookstore_page = BookstorePage(page)


