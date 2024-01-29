from playwright.sync_api import Page
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("PROFILE_PAGE_URL")

class ProfilePage:

    def __init__(self, page):
        self.page = page
        self.url = url


    def go_to_bookstore(self):
        self.page.get_by_role("button", name="Go To Book Store").click()


#    def get_user_books(self):

#    def get_user_name(self):

#    def delete_book(self):

#    def delete_all_books(self):


