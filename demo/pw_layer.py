from playwright.sync_api import Page, expect, sync_playwright


def pw1_baidu():
    # pw = sync_playwright().start()
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url="https://www.baidu.com")
        # page.wait_for_timeout(5_000)
        page.locator('//input[@name="wd"]').fill("playwright")
        page.get_by_text("百度一下").click()
        expect(page.get_by_text("https://github.com/microsoft/playwright")).to_be_visible()


def pw2_baidu():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url="https://www.baidu.com")
    # page.wait_for_timeout(5_000)
    page.locator('//input[@name="wd"]').fill("playwright")
    page.get_by_text("百度一下").click()
    expect(page.get_by_text("https://github.com/microsoft/playwright")).to_be_visible()
    pw.stop()


pw1_baidu()
pw2_baidu()