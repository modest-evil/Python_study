from dotenv import load_dotenv
import os
from playwright.sync_api import Page

load_dotenv()
url = os.getenv("URL")

def get_booklist(page: Page):
    action_button_list = page.locator('.mr-2 > a').all_text_contents()

    return action_button_list

def get_book_links(page: Page, booklist):
    link_list = []

    for Name in booklist:
        link_list.append(page.get_by_role("link", name=Name).get_attribute("href"))

    return link_list

def get_list_of_isbns(link_list):
    isbns = []

    for link in link_list:
        isbns.append(link.removeprefix("/profile?book="))

    return isbns

# for isbn only
# a = "12:14 = abcdef"
# print(a.removeprefix("12:14 ="))




