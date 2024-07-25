from testcases import *


def test_storage_state(browser: Browser):
    # my_page = PageIns(page)
    # my_page.登录页.登录("winni", "playwright001")
    # my_page.page.context.storage_state(path="winni.json")
    context = browser.new_context(storage_state="winni.json")
    page = context.new_page()
    page.goto("https://playwright.ezone.work/workbench/workCalendar?date=20240720&viewType=calendar&viewUnit=month")