from playwright.sync_api import Page
from Tests.UI.test_helpers import Booklist_functions
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")

class BookstorePage:

    def __init__(self, page):
        self.page = page
        self.url = url + "/books"

    def open(self):
        self.page.goto(self.url)

    def log_out(self):
        self.page.get_by_role("button", name="Log out").click()

    def get_books(self):
        return Booklist_functions.get_booklist(self.page)

    def search(self, to_search):
        self.page.get_by_placeholder("Type to search").click()
        self.page.get_by_placeholder("Type to search").fill(to_search)
        self.page.get_by_placeholder("Type to search").press("Enter")

    def select_book(self, book_title):
        self.page.get_by_role("link", name=book_title).click()


    def back_to_bookstore(self):
        self.page.get_by_role("button", name="Back To Book Store").click()






