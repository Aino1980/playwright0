from testcases import *


def test_重试机制_while_for_try(new_context):
    with 测试步骤("尝试登录并跳转"):
        my_page_测试员 = PageIns.使用new_context登录并返回实例化的page(new_context, "测试员")
        my_page_测试员.项目集.navigate()
    # with 测试步骤("普通悬浮操作"):
    # my_page_测试员.page.locator(".ant-dropdown-trigger").hover()
    # my_page_测试员.page.wait_for_timeout(3_000)
    # my_page_测试员.page.get_by_text("个人主页").click(timeout=3_000)

    # with 测试步骤("带重试的悬浮操作"):
    #     my_page_测试员.项目集.hover_retry(my_page_测试员.page.locator(".ant-dropdown-trigger"), my_page_测试员.page.get_by_text("个人主页11"))

    with 测试步骤("使用封装的通用重试来做悬浮的重试操作"):
        my_page_测试员.项目集.重试((my_page_测试员.page.mouse.move, 1, 1),
                                   (my_page_测试员.page.wait_for_timeout, {"timeout": 1_000}),
                                   my_page_测试员.page.locator(".ant-dropdown-trigger").hover,
                                   (my_page_测试员.page.get_by_text("个人主页11").click, {"timeout": 1_000})
                                   )
