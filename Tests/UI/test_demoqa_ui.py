import re
import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     browser = playwright.firefox.launch()
#     page = browser.new_page()
#     page.goto("https://demoqa.com/login")

#pytest test_demoqa_ui.py --browser firefox

# @pytest.fixture(scope="function", autouse=True)
# def before_each_after_each(page: Page):
#
#     print("before the test runs")
#
#     # Go to the starting url before each test.
#     page.goto("https://demoqa.com/login")
#     yield
#
#     print("after the test runs")

def test_main_navigation(page: Page):

    page.goto("https://demoqa.com/login")
    expect(page).to_have_url("https://demoqa.com/login")


def test_user_login(page: Page):

    # with sync_playwright() as playwright:
    #     browser = playwright.firefox.launch(headless=False)
    #     page = browser.new_page()
    #     page.goto("https://demoqa.com/login")

    page.goto("https://demoqa.com/login")

    username_field = page.get_by_label("userName")
    username_field.fill("Anne")
    page.get_by_label("password").fill("Anne123!")

    page.get_by_role("button", name="login").click()

    expect(page).to_have_url("https://demoqa.com/profile")
    expect(page.get_by_label("userName-value")).to_have_value("Anne")


def test_user_add_book(page: Page):
    page.goto("https://demoqa.com/profile")

    page.get_by_role("button", name="gotoStore").click(force=True)

    expect(page).to_have_url("https://demoqa.com/books")
