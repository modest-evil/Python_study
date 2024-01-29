from playwright.sync_api import Page
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("BOOKSTORE_PAGE_URL")

class BookstorePage:

    def __init__(self, page):
        self.page = page
        self.url = url


    def get_books(self):
        self.page.goto(url)
        # get list of booknames associated with urls


    def add_book(self):
        self.page.get_by_role("link", name="Git Pocket Guide").click()
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.get_by_role("button", name="Add To Your Collection").click()
        self.page.get_by_role("button", name="Back To Book Store").click()


    # def bookstore_search(self):
    #
    # def get_booklist(self):
    #
    # def select_book(self):
    #
    # def add_chosen_book(self):

