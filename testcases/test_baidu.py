from testcases import *


def test_baidu(page: Page):
    my_page = PageIns(page)
    # baidu.navigate()
    # baidu.search_input.fill("playwright")
    # baidu.click_button("百度一下")
    # expect(baidu.page.get_by_text("https://github.com/microsoft/playwright").last).to_be_visible()
    my_page.百度.baidu_search("playwright", "https://github.com/microsoft/playwright")
