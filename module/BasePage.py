import os.path
from module import *
from utils.globalMap import GlobalMap


class PageObject:
    def __init__(self, page: Page):
        self.page = page
        self.url = ""

    def navigate(self):
        self.page.goto(self.url)

    def click_button(self, button_name, timeout=30_000):
        button_loc = self.page.locator("button")
        for 单字符 in button_name:
            button_loc = button_loc.filter(has_text=单字符)
        button_loc.click(timeout=timeout)


def 使用new_context登录并返回实例化的page(new_context, 用户别名):
    from module.PageInstance import PageIns
    global_map = GlobalMap()
    被测环境 = global_map.get("env")
    用户名 = MyData().userinfo(被测环境, 用户别名)["username"]
    密码 = MyData().userinfo(被测环境, 用户别名)["password"]
    with FileLock(get_path(f".temp/{被测环境}-{用户别名}.lock")):
        if os.path.exists(get_path(f".temp/{被测环境}-{用户别名}.json")):
            context: BrowserContext = new_context(storage_state=get_path(f".temp/{被测环境}-{用户别名}.json"))
            page = context.new_page()
            my_page = PageIns(page)
            my_page.我的任务.navigate()
            expect(my_page.登录页.用户名输入框.or_(my_page.登录页.通知铃铛)).to_be_visible()
            if my_page.登录页.用户名输入框.count():
                my_page.登录页.登录(用户名, 密码)
                my_page.page.context.storage_state(path=get_path(f".temp/{被测环境}-{用户别名}.json"))
        else:
            context: BrowserContext = new_context()
            page = context.new_page()
            my_page = PageIns(page)
            my_page.登录页.登录(用户名, 密码)
            my_page.page.context.storage_state(path=get_path(f".temp/{被测环境}-{用户别名}.json"))
    return my_page

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





