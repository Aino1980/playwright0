from testcases import *


def test_重试机制_while_for_try(new_context):
    with 测试步骤("尝试登录并跳转"):
        my_page_测试员 = PageIns.使用new_context登录并返回实例化的page(new_context, "测试员")
        my_page_测试员.项目集.navigate()
        my_page_测试员.项目集.click_button("新建")
    # with 测试步骤("正常下拉框操作"):
    #     my_page_测试员.page.locator("#parent").click()
    #     my_page_测试员.page.get_by_title("公共项目集").click()
    #     my_page_测试员
    #
    # with 测试步骤("使用for和try来重试下拉框"):
    #     for _ in range(4):
    #         if _ == 3:
    #             pytest.fail("下拉框三次重试还是失败")
    #         try:
    #             my_page_测试员.page.locator("#parent").blur()
    #             my_page_测试员.page.locator("#parent").click()
    #             my_page_测试员.page.wait_for_timeout(3_000)
    #             my_page_测试员.page.get_by_title("公共项目集").click(timeout=2_000)
    #             break
    #         except:
    #             pass
    #
    with 测试步骤("使用while和try来重试下拉框"):
        start_time = time.time()
        while True:
            if time.time() - start_time > 30:
                pytest.fail("下拉框30秒内重试还是失败")
            try:
                my_page_测试员.page.locator("#parent").blur()
                my_page_测试员.page.locator("#parent").click()
                my_page_测试员.page.wait_for_timeout(3_000)
                my_page_测试员.page.get_by_title("公共项目集").click(timeout=2_000)
                break
            except:
                pass
