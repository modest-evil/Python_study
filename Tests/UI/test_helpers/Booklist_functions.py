from dotenv import load_dotenv
import os
from playwright.sync_api import Page

load_dotenv()
url = os.getenv("URL")

def get_booklist(page: Page):
    url = page.url
