import re
import pytest
from playwright.sync_api import Page, expect

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
