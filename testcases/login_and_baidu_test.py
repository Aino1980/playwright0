from testcases import *


def test_login_and_baidu(page: Page):
    my_page = PageIns(page)
    my_page.登录页.登录("winni", "playwright001")
    my_page.百度.baidu_search("playwright", "https://github.com/microsoft/playwright")