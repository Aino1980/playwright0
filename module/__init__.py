import pytest
import time
import os
import sys
import re
import random
from playwright.sync_api import Page, expect, BrowserContext, Locator
from module.BasePage import PageObject
from utils.GetPath import get_path
from filelock import FileLock
from data_module.auth_Data import MyData
from utils.globalMap import GlobalMap
from module.BaiduPage import Baidu
from module.登录页 import 登录页_类
from module.我的任务 import 我的任务_类
from module.项目集 import 项目集_类


class PageIns:
    def __init__(self, page: Page):
        self.page = page
        self.百度 = Baidu(self.page)
        self.登录页 = 登录页_类(self.page)
        self.我的任务 = 我的任务_类(self.page)
        self.项目集 = 项目集_类(self.page)

    @staticmethod
    def 使用new_context登录并返回实例化的page(new_context, 用户别名):
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