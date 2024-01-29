import re
import pytest
from playwright.sync_api import Page, expect

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
