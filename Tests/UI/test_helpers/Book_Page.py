from playwright.sync_api import Page
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")

class BookPage():

    def __init__(self, page, isbn):
        self.page = page
        self.url = url + "/books?book=" + isbn

    def open(self):
        self.page.goto(self.url)

    def back_to_bookstore(self):
        self.page.get_by_role("button", name="Back To Book Store").click()

    def add_book(self):
        self.page.get_by_role("button", name="Add To Your Collection").click()
        self.page.once("dialog", lambda dialog: dialog.dismiss())

    def log_out(self):
        self.page.get_by_role("button", name="Log out").click()

