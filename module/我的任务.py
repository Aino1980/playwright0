from module import *


class 我的任务_类(PageObject):
    def __init__(self, page):
        super().__init__(page)
        self.url = "/workbench/mytask"
        self.通知铃铛 = self.page.locator(".anticon-bell")

