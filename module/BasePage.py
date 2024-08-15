from module import *
from module.table import Table


class PageObject:
    def __init__(self, page: Page):
        self.page = page
        self.url = ""

    def navigate(self):
        self.page.goto(self.url)

    def table(self, 唯一文字, 表格序号=-1):
        return Table(self.page, 唯一文字, 表格序号)

    def click_button(self, button_name, timeout=30_000):
        button_loc = self.page.locator("button")
        for 单字符 in button_name:
            button_loc = button_loc.filter(has_text=单字符)
        button_loc.click(timeout=timeout)

    def search(self, 搜索内容: str, placeholder=None):
        if placeholder:
            self.page.locator(f"//span[@class='ant-input-affix-wrapper']//input[contains(@placeholder,'{placeholder}')]").fill(搜索内容)
        else:
            self.page.locator(".ant-input-affix-wrapper input").fill(搜索内容)
        self.page.wait_for_load_state("networkidle")


    # with f"这里使用filelock进行文件锁,锁的文件名字为{被测环境}-{用户别名}.lock":
    #     if f".temp/{被测环境}-{用户别名}.json存在,判断方法os.path.exists":
    #         context = new_context(storage_state=f".temp/{被测环境}-{用户别名}.json")
    #         page = context.new_page
    #         my_page = "PageIns实例化page,获得所有页面的操控方法"
    #         # 需要新增一个首页的封装
    #         my_page.首页.navigate()
    #         登录成功 = "判断下是成功登录上了,还是登录失败"
    #         if not 登录成功:
    #             my_page.登录页.登录(用户名, 密码)
    #             f"把storage_state保存为.temp/{被测环境}-{用户别名}.json"
    #     else:
    #         context = new_context()
    #         page = context.new_page
    #         my_page = "PageIns实例化page,获得所有页面的操控方法"
    #         my_page.登录页.登录(用户名, 密码)
    #         f"把storage_state保存为.temp/{被测环境}-{用户别名}.json"
    # return my_page





