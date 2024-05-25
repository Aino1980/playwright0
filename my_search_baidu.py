from playwright.sync_api import Page


def test_baidu(page: Page):
    page.goto(url="https://www.baidu.com")
    page.wait_for_timeout(5_000)
