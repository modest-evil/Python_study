from dotenv import load_dotenv
import os
from playwright.sync_api import Page

load_dotenv()
url = os.getenv("URL")

def get_booklist(page: Page):
    #texts = page.get_by_role("link").all_inner_texts()

    action_button_list = page.locator('.mr-2').all_inner_texts()
    count = action_button_list.count()



# for isbn only
# a = "12:14 = abcdef"
# print(a.removeprefix("12:14 ="))




