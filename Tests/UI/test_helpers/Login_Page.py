from playwright.sync_api import Page
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.url = url + "/login"

    def open(self):
        self.page.goto(self.url)

    def fill_username(self, name):
        self.page.get_by_placeholder("UserName").click()
        self.page.get_by_placeholder("UserName").fill(name)

    def fill_password(self, password):
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill(password)

    def click_login(self):
        self.page.get_by_role("button", name="Login").click()

    def log_in(self, name, password):
        self.fill_username(name)
        self.fill_password(password)
        self.click_login()
