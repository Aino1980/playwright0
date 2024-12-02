from playwright.sync_api import Playwright, Request


def test_network_monitor(playwright: Playwright):
    def on_context(req: Request):
        if "www.baidu.com" in req.url:
            print(req.url)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.on("request", on_context)
    page = context.new_page()
    page.goto("http://www.baidu.com")