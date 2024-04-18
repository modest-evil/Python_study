from playwright.sync_api import Page, expect
from Tests.UI.test_helpers.Pages.Login_Page import LoginPage
from Tests.UI.test_helpers.Pages.Profile_Page import ProfilePage
from Tests.UI.test_fixtures.ui_fixtures import before_test
from Tests.UI.test_fixtures.ui_fixtures import user_logged_in
from dotenv import load_dotenv
import os

load_dotenv()
test_username = os.getenv("TESTUSER")
test_password = os.getenv("PASSWORD")
start_page = os.getenv("LOGIN_PAGE_URL")

def test_user_delete_account(user_logged_in, before_test):
    user = before_test
    user.save_user = True

    profile_page = ProfilePage(user_logged_in)
    profile_page.open()
    profile_page.delete_account()

    expect(user_logged_in).to_have_url(start_page)
