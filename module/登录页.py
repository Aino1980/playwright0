from module import *


class 登录页_类(PageObject):
    def __init__(self, page):
        super().__init__(page)
        self.url = "/signin"
        self.用户名输入框 = self.page.get_by_placeholder("用户名/邮箱/手机号")
        self.密码输入框 = self.page.get_by_placeholder("密码")
        self.通知铃铛 = self.page.locator(".anticon-bell")

    def 登录(self, 用户名, 密码):
        self.navigate()
        self.用户名输入框.fill(用户名)
        self.密码输入框.fill(密码)
        self.click_button("登录")
        expect(self.通知铃铛).to_be_visible()




