import re
import pytest
from playwright.sync_api import Page, expect
from Tests.UI.test_helpers.Login_Page import LoginPage


def test_log_in_user_exists(page: Page):
    page.goto("https://demoqa.com/login")

    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill("Anne")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Anne123!")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://demoqa.com/profile")
   # expect(page.get_by_label("userName-value")).to_have_value("Anne")
    page.get_by_text("Anne").click()


def test_log_in_page(page: Page):
    login_page = LoginPage(page)
    login_page.log_in("Anne", "Anne123!")

    expect(page).to_have_url("https://demoqa.com/profile")

