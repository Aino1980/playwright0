from testcases import *


def test_filelock2(page: Page):
    my_page = PageIns(page)
    with FileLock(get_path("/.temp/lock.loc")):
        my_page.百度.baidu_search("playwright", "https://github.com/microsoft/playwright")
        # page.wait_for_timeout(10_000)
        global_map = GlobalMap()
        global_map.set("b", 456)
        # assert global_map.get("a") == 123
        assert global_map.get("b") == 456