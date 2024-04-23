import re
import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from Tests.UI.test_helpers import Booklist_functions
import Tests.UI.test_helpers.Booklist_functions

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
# there is no context here cause user is NOT logged in, nothing to collect from context
# still have no session token
#    else :
#         latecontext = page.context.storage_state()
#         cookie = latecontext["cookies"]
#
#         user.userId = list(filter(lambda x: x['name'] == 'userID', cookie))[0]['value']
#         user.sessionToken = list(filter(lambda x: x['name'] == 'token', cookie))[0]['value']

    # if not user.save_user:
    #     user.delete_account(user.sessionToken, user.userId)

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

#    page.goto("https://demoqa.com/books")

    #print(Booklist_functions.get_booklist(page))
    linklist = []

#    action_button_list = page.locator('.mr-2').locator('a').all_inner_texts()
    action_button_list = page.locator('.mr-2 > a').all_text_contents()

    button_list = Booklist_functions.get_booklist(page)

    link = page.get_by_role("link", name=button_list[0]).get_attribute("href")

    links = Booklist_functions.get_book_links(page, button_list)

    isbns = Booklist_functions.get_list_of_isbns(links)

#    action_button_list = page.locator('.mr-2 > a').inner_html()
#    for li in page.locator('.mr-2').locator('a'):
 #   for li in page.locator('.mr-2'):
 #       linklist.append(li.get_attribute('a'))
 #   action_link_list = page.locator('.mr-2').locator('a').get_attribute('href')

    # linkslist = page.locator('.mr-2 > a')
    for links in page.locator('.mr-2 > a').element_handle():
        linkF = links.get_attribute("href")
        linklist.append(linkF)

#    hrefs_of_page = page.eval_on_selector_all("a[href^='/profile?book=']", "elements => elements.map(element => element.href)")

    hrefs = page.get_by_role("link")

    count = len(action_button_list)
    ncount = len(button_list)
    print(action_button_list)

    assert count == 4
    assert ncount == 4
