from module import *


class PageObject:
    def __init__(self, page: Page):
        self.page = page
        self.url = ""

    def navigate(self):
        self.page.goto(self.url)

    def click_button(self, button_name, timeout=30_000):
        self.page.get_by_role("button").filter(has_text=button_name).click(timeout=timeout)