from testcases import *


@pytest.mark.browser_context_args(timezone_id="Europe/Berlin", locale="en-GB")
def test_new_context(new_context):
    my_page_测试员 = PageIns.使用new_context登录并返回实例化的page(new_context, "测试员")
    my_page_项目经理 = PageIns.使用new_context登录并返回实例化的page(new_context, "项目经理")
    my_page_项目经理.page.wait_for_timeout(5_000)