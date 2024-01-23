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


def test_login_autogen(page: Page):
    # browser = page.firefox.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://demoqa.com/login")
    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill("Anne")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Anne123!")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://demoqa.com/profile")
   # expect(page.get_by_label("userName-value")).to_have_value("Anne")
    page.get_by_text("Anne").click()

def test_add_book(page: Page):
    #login
    page.goto("https://demoqa.com/login")
    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill("Anne")
    page.get_by_placeholder("UserName").press("Tab")
    page.get_by_placeholder("Password").fill("Anne123!")
    page.get_by_role("button", name="Login").click()

    #add book
    page.get_by_role("button", name="Go To Book Store").click()
    page.get_by_role("link", name="Git Pocket Guide").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add To Your Collection").click()
    page.get_by_role("button", name="Back To Book Store").click()

    #add one more book
    page.get_by_role("link", name="Learning JavaScript Design").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add To Your Collection").click()
    page.get_by_role("button", name="Back To Book Store").click()

    #go to profile check you have books
    page.locator("li").filter(has_text="Profile").click()


def test_delete_book(page: Page):
    #login
    page.goto("https://demoqa.com/login")
    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill("Anne")
    page.get_by_placeholder("UserName").press("Tab")
    page.get_by_placeholder("Password").fill("Anne123!")
    page.get_by_role("button", name="Login").click()

    #add one book
    page.get_by_role("button", name="Go To Book Store").click()
    page.get_by_role("link", name="Git Pocket Guide").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add To Your Collection").click()
    page.get_by_role("button", name="Back To Book Store").click()

    #add one more book
    page.get_by_role("link", name="Learning JavaScript Design").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add To Your Collection").click()
    page.get_by_role("button", name="Back To Book Store").click()

    #delete book
    page.get_by_text("Profile").click()
    page.get_by_role("row", name="image Git Pocket Guide").locator("path").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="OK").click()

    #check you have no deleted book


def test_delete_all_books(page: Page):
    #login
    page.goto("https://demoqa.com/login")
    page.get_by_placeholder("UserName").click()
    page.get_by_placeholder("UserName").fill("Anne")
    page.get_by_placeholder("UserName").press("Tab")
    page.get_by_placeholder("Password").fill("Anne123!")
    page.get_by_role("button", name="Login").click()

    #add book
    page.get_by_role("button", name="Go To Book Store").click()
    page.get_by_role("link", name="Git Pocket Guide").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add To Your Collection").click()
    page.get_by_role("button", name="Back To Book Store").click()

    #add one more book
    page.get_by_role("link", name="Learning JavaScript Design").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add To Your Collection").click()
    page.get_by_role("button", name="Back To Book Store").click()

    #delete all books
    page.get_by_text("Profile").click()
    page.get_by_role("button", name="Delete All Books").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="OK").click()

    #check there is no books

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