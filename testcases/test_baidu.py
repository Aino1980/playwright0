from testcases import *


def test_baidu(page: Page):
    my_page = PageIns(page)
    my_page.百度.baidu_search("淘宝", "淘宝")
    with my_page.page.expect_popup() as new:
        my_page.百度.page.locator("a").filter(has_text="淘宝").first.click()
    print(my_page.百度.page.title())
    my_page.page = new.value
    my_page.百度.page.wait_for_timeout(3_000)
    print(my_page.百度.page.title())