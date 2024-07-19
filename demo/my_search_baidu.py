from playwright.sync_api import Page, expect


def test_baidu(page: Page):
    page.goto(url="https://www.baidu.com")
    # page.wait_for_timeout(5_000)
    page.locator('//input[@name="wd"]').fill("playwright")
    page.get_by_text("百度一下").click()
    expect(page.get_by_text("https://github.com/microsoft/playwright")).to_be_visible()