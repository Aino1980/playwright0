from testcases import *


def test_login(page: Page):
    my_page = PageIns(page)
    my_page.登录页.登录("winni", "playwright001")
    my_page.page.wait_for_timeout(5_000)