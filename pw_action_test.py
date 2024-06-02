from playwright.sync_api import Page, expect


def test_pw_click(page: Page):
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
    page.goto("/demo/button")
    page.wait_for_timeout(3_000)
    page.get_by_text("点击我试试1").click()
    expect(page.get_by_text("点击成功1!")).to_be_visible()
