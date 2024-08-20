from module import *


class Locators:
    def __init__(self, page: Page):
        self.page = page

    def button_按钮(self, text, nth=-1) -> Locator:
        button = self.page.locator("button")
        for word in text:
            button = button.filter(has_text=word)
        return button.locator('visible=true').nth(nth)

    def below_元素下方紧邻的元素(self, 要找的元素类型="*") -> Locator:
        return self.page.locator(f"xpath=/following::{要找的元素类型}[position()=1]")

    def 表单项中包含操作元素的最上级div(self, 字段名: str) -> Locator:
        最终上级元素locator = self.page.locator("label").locator("visible=true").filter(has=self.page.get_by_text(字段名)).locator(self.below_元素下方紧邻的元素())
        return 最终上级元素locator


