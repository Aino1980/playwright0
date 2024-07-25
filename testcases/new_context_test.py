from testcases import *


@pytest.mark.browser_context_args(storage_state="winni.json")
def test_new_context(page: Page, new_context):
    # context1: BrowserContext = new_context(storage_state="winni.json")
    # context1.new_page().goto("/workbench/myapproval")
    # context2: BrowserContext = new_context()
    # context2.new_page().goto("/workbench/myapproval")
    page.goto("/workbench/myapproval")



