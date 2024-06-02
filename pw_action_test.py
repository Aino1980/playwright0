from playwright.sync_api import Page, expect


def test_pw_action(page: Page):
    page.goto("/demo/button")
    page.wait_for_timeout(1_000)
