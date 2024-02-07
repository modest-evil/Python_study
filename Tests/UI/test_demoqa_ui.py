import re
import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from Tests.UI.test_helpers import Booklist_functions

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


def test_create_user(page: Page):
    #create user
    page.goto("https://demoqa.com/login")
    page.get_by_role("button", name="New User").click()
    page.get_by_placeholder("First Name").click()
    page.get_by_placeholder("First Name").fill("Bobby")
    page.get_by_placeholder("First Name").press("Tab")
    page.get_by_placeholder("Last Name").fill("Halt")
    page.get_by_placeholder("Last Name").press("Tab")
    page.get_by_placeholder("UserName").fill("Bobby")
    page.get_by_placeholder("UserName").press("Tab")
    page.get_by_placeholder("Password").fill("Bobby123!")
    page.frame_locator("iframe[name=\"a-m056fh5hi0ig\"]").get_by_label("I'm not a robot").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    expect(page).to_have_url("https://demoqa.com/register")
    page.get_by_role("button", name="Register").click()

    #login
    page.get_by_role("button", name="Back to Login").click()
    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill("Bobby")
    page.get_by_placeholder("UserName").press("Tab")
    page.get_by_placeholder("Password").fill("Bobby123!")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://demoqa.com/profile")

    #logout
    page.get_by_role("button", name="Log out").click()
    expect(page).to_have_url("https://demoqa.com/login")


def test_list_of_books(page: Page):
    page.goto("https://demoqa.com/login")

    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill("Anne")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Anne123!")
    page.get_by_role("button", name="Login").click()

    #print(Booklist_functions.get_booklist(page))
    linklist = []

#    action_button_list = page.locator('.mr-2').locator('a').all_inner_texts()
    action_button_list = page.locator('.mr-2 > a').all_inner_texts()
    for li in page.locator('.mr-2').locator('a'):
        linklist.append(li.get_attribute('href'))
 #   action_link_list = page.locator('.mr-2').locator('a').get_attribute('href')
    count = len(action_button_list)
    print(action_button_list)

    assert count == 4
