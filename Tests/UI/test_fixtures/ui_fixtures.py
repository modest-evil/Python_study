import pytest

from playwright.sync_api import sync_playwright, Playwright
from playwright.sync_api import Page, expect
from Tests.API.test_helpers.user_funcs import User
from Tests.API.test_helpers.bookstore_funcs import Bookstore
from Tests.UI.test_helpers.Pages.Login_Page import LoginPage
from Tests.UI.test_helpers.Pages.Profile_Page import ProfilePage
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")
test_username = os.getenv("TESTUSER")
test_password = os.getenv("PASSWORD")
profile = os.getenv("PROFILE_PAGE_URL")


@pytest.fixture()
def before_test(page):
    user = User(url)
    yield user

    if not user.save_user:
        user.log_in(user.username, user.password)
        user.delete_account(user.sessionToken, user.userId)


@pytest.fixture(params=[(test_username, test_password)])
def user_logged_in(request, before_test, page, browser):
    username, password = request.param
    before_test.create_user(username, password)

    page.context.close()
    context = browser.new_context()
    n_page = context.new_page()

    login_page = LoginPage(n_page)
    login_page.open()
    login_page.log_in(username, password)
    expect(n_page).to_have_url(profile)

    storage = n_page.context.storage_state(path="state.json")
    context.close()

    context = browser.new_context(storage_state="state.json")
    restored_page = context.new_page()

    yield restored_page


@pytest.fixture(params=[(test_username, test_password)])
def user_exists_has_books(request, before_test, page, browser):
    username, password = request.param
    before_test.create_user(username, password)
    before_test.log_in(username, password)

    shelf = Bookstore(url)
    isbns = shelf.get_booklist()
    isbn1 = isbns.pop(0)
    isbn2 = isbns.pop(1)
    isbn3 = isbns.pop(2)

    shelf.add_books(before_test.userId, before_test.sessionToken, isbn1)
    shelf.add_books(before_test.userId, before_test.sessionToken, isbn2)
    shelf.add_books(before_test.userId, before_test.sessionToken, isbn3)

    # login from UI and restore session
    # use for delete book and delete all books test

    page.context.close()
    context = browser.new_context()
    n_page = context.new_page()

    login_page = LoginPage(n_page)
    login_page.open()
    login_page.log_in(username, password)
    expect(n_page).to_have_url(profile)

    storage = n_page.context.storage_state(path="state.json")

    context.close()

    context = browser.new_context(storage_state="state.json")
    restored_page = context.new_page()

    yield restored_page
