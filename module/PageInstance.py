from module import *


class PageIns:
    def __init__(self, page: Page):
        self.page = page
        self.百度 = Baidu(self.page)
        self.登录页 = 登录页_类(self.page)
        self.我的任务 = 我的任务_类(self.page)