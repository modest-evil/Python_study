from playwright.sync_api import Page
from Tests.UI.test_helpers import Booklist_functions
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")

class ProfilePage:

    def __init__(self, page):
        self.page = page
        self.url = url + "/profile"

    def open(self):
        self.page.goto(self.url)

    def log_out(self):
        self.page.get_by_role("button", name="Log out").click()

    def go_to_bookstore(self):
        self.page.get_by_role("button", name="Go To Book Store").click()

    def search(self, to_search):
        self.page.get_by_placeholder("Type to search").click()
        self.page.get_by_placeholder("Type to search").fill(to_search)
        self.page.get_by_placeholder("Type to search").press("Enter")


    def get_user_books(self):
        return Booklist_functions.get_booklist(self.page)

    # def get_user_name(self):
    #     return self.page.get_by_label("userName-value")

    def delete_book(self, book_title):
        self.page.get_by_role("row", name="image " + book_title).locator("path").click()
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.get_by_role("button", name="OK").click()

    def delete_all_books(self):
        self.page.get_by_role("button", name="Delete All Books").click()
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.get_by_role("button", name="OK").click()



