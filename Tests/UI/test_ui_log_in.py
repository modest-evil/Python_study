from playwright.sync_api import Page, expect
from Tests.UI.test_helpers.Pages.Login_Page import LoginPage
from Tests.UI.test_fixtures.ui_fixtures import before_test
from dotenv import load_dotenv
import os

load_dotenv()
test_username = os.getenv("TESTUSER")
test_password = os.getenv("PASSWORD")
profile = os.getenv("PROFILE_PAGE_URL")

# name = os.getenv("UI_TEST_USER")
# password = os.getenv("UI_TEST_PASS")


# def test_log_in_user_exists(page: Page):
#     page.goto("https://demoqa.com/login")
#
#     page.get_by_placeholder("UserName").click()
#     page.get_by_placeholder("UserName").fill("Anne")
#     page.get_by_placeholder("Password").click()
#     page.get_by_placeholder("Password").fill("Anne123!")
#     page.get_by_role("button", name="Login").click()
#
#     expect(page).to_have_url("https://demoqa.com/profile")
#     page.get_by_text("Anne").click()


def test_log_in(before_test, page: Page):
    before_test.create_user(test_username, test_password)

    login_page = LoginPage(page)
    login_page.open()
    login_page.log_in(test_username, test_password)

    expect(page).to_have_url(profile)
    expect(page.get_by_text("User Name :")).to_be_visible()
    expect(page.get_by_text(test_username)).to_be_visible()

