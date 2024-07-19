import os.path
import pytest

from playwright.sync_api import Page, expect


@pytest.mark.only
def test_pw_click(page: Page, hello_world):
    page.goto("/demo/button")
    page.get_by_text("点击我试试1").click(modifiers=["Control"])
    page.get_by_text("点击我试试1").click(position={"x": 15, "y": 20})
    page.get_by_text("点击我试试1").click(button="right")
    page.get_by_text("点击我试试1").click(click_count=3, delay=1_000)
    page.get_by_text("点击我试试1").click(timeout=3_000)
    page.get_by_text("点击我试试1").click(force=True)
    page.get_by_text("点击我试试1").click(no_wait_after=True)
    page.get_by_text("点击我试试1").click(trial=True)
    page.get_by_text("点击我试试1").dblclick()


def test_pw_notification_message(page: Page):
    page.goto("/demo/button", wait_until="networkidle")
    # page.wait_for_timeout(3_000)
    page.get_by_text("点击我试试1").click()
    expect(page.get_by_text("点击成功1!")).to_be_visible()


def test_pw_new_page(page: Page):
    page.goto("/demo/link", wait_until="networkidle")
    page.get_by_text("本页跳转到百度").click()
    expect(page.get_by_text("百度一下", exact=True)).to_be_visible()
    page.goto("/demo/link", wait_until="networkidle")
    with page.expect_popup() as new_page:
        page.get_by_text("新页面跳转到淘宝").click()
    page_new = new_page.value
    expect(page_new.locator(".search-button")).to_be_attached()


def test_pw_hover(page: Page):
    page.goto("/demo/hover", wait_until="networkidle")
    page.locator("#c4").hover()
    expect(page.get_by_text("你已经成功悬浮")).to_be_visible()


def test_pw_dropdown(page: Page):
    page.goto("/demo/dropdown", wait_until="networkidle")
    page.get_by_text("点击选择").click()
    page.get_by_text("playwright").click()
    expect(page.get_by_text("你选择了websocket")).to_be_visible()
    page.get_by_text("点击选择").click()
    page.get_by_text("selenium").click()
    expect(page.get_by_text("你选择了webdriver")).to_be_visible()


def test_pw_input(page: Page):
    page.goto("/demo/input", wait_until="networkidle")
    page.get_by_placeholder("不用管我,我是placeholder").fill("12345")
    page.get_by_label("也许你可以").fill("label定位")
    page.get_by_label("数字输入专用").fill("123.1234567812345678")
    page.get_by_label("数字输入专用").blur()
    page.wait_for_timeout(1_000)
    assert page.get_by_label("数字输入专用").input_value() == "123.1234567812"


def test_pw_textarea(page: Page):
    page.goto("/demo/textarea", wait_until="networkidle")
    page.locator("textarea").fill("12345")
    page.locator("textarea").fill("123\n45")
    page.locator("textarea").fill("""123
456""")
    expect(page.locator("textarea")).to_have_value("123\n456")
    page.locator("textarea").press_sequentially("789", delay=1_000)
    expect(page.locator("textarea")).to_have_value("123\n456789")


def test_pw_radio(page: Page):
    page.goto("/demo/radio", wait_until="networkidle")
    page.get_by_text("草莓").locator("input").check()
    expect(page.get_by_text("草莓").locator("input")).to_be_checked()
    page.wait_for_timeout(1_000)
    page.get_by_text("香蕉").locator("input").check()
    expect(page.get_by_text("香蕉").locator("input")).to_be_checked()
    page.wait_for_timeout(1_000)
    page.get_by_text("苹果").locator("input").check()
    expect(page.get_by_text("苹果").locator("input")).to_be_checked()
    page.wait_for_timeout(1_000)


def test_pw_checkbox(page: Page):
    page.goto("/demo/checkbox", wait_until="networkidle")
    page.get_by_text("开发").locator("input").set_checked(True)
    expect(page.get_by_text("开发").locator("input")).to_be_checked()
    page.wait_for_timeout(1_000)
    page.get_by_text("测试").locator("input").set_checked(True)
    expect(page.get_by_text("测试").locator("input")).to_be_checked()
    page.wait_for_timeout(1_000)
    page.get_by_text("美团").locator("input").set_checked(True)
    expect(page.get_by_text("美团").locator("input")).to_be_checked()
    page.wait_for_timeout(1_000)
    page.get_by_text("开发").locator("input").set_checked(False)
    expect(page.get_by_text("开发").locator("input")).not_to_be_checked()
    page.wait_for_timeout(1_000)
    page.get_by_text("测试").locator("input").set_checked(False)
    expect(page.get_by_text("测试").locator("input")).not_to_be_checked()
    page.wait_for_timeout(1_000)
    page.get_by_text("美团").locator("input").set_checked(False)
    expect(page.get_by_text("美团").locator("input")).not_to_be_checked()
    page.wait_for_timeout(1_000)


def test_pw_switch(page: Page):
    page.goto("/demo/switch", wait_until="networkidle")
    page.locator('//div[@aria-checked]').click()
    expect(page.locator('//div[@aria-checked="true"]')).to_be_visible()
    expect(page.get_by_text("已经学会了~")).to_be_visible()
    page.locator('//div[@aria-checked]').click()
    expect(page.locator('//div[@aria-checked="false"]')).to_be_visible()


def test_pw_upload(page: Page):
    page.goto("/demo/upload", wait_until="networkidle")
    page.locator('//input[@type="file"]').set_input_files("my_search_baidu.py")
    expect(page.get_by_text("uploaded").last).to_be_visible()
    with page.expect_file_chooser() as chooser:
        page.locator("a").last.click()
    chooser.value.set_files("pytest.ini")
    expect(page.get_by_text("uploaded").last).to_be_visible()
    page.wait_for_timeout(5_000)


def test_pw_download(page: Page):
    page.goto("/demo/download", wait_until="networkidle")
    page.locator("textarea").fill("123456")
    with page.expect_download() as file:
        page.get_by_text("Download").click()
    file.value.save_as("123.txt")
    assert os.path.exists("123.txt")


def test_pw_drag(page: Page):
    page.goto("/demo/drag", wait_until="networkidle")
    page.get_by_text("去壶口瀑布").drag_to(page.get_by_text("正在做"))
    expect(page.get_by_text("正在做").locator("xpath=/..").get_by_text("去壶口瀑布").last).to_be_visible()

    page.get_by_placeholder("请选择品类哈哈").locator("visible=true").count()
    page.get_by_placeholder("请选择品类").locator("visible=true").count()
