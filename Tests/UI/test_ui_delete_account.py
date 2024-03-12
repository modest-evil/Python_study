from playwright.sync_api import Page, expect
from Tests.UI.test_helpers.Pages.Login_Page import LoginPage
from Tests.API.test_fixtures.demoqa_fixtures import cleanup
from Tests.API.test_fixtures.demoqa_fixtures import create_account
from Tests.UI.test_fixtures.ui_fixtures import before_test
from dotenv import load_dotenv
import os

load_dotenv()
test_username = os.getenv("TESTUSER")
test_password = os.getenv("PASSWORD")

