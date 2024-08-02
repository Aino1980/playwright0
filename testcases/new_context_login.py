from testcases import *


def test_new_context(new_context):
    my_page_测试员 = 使用new_context登录并返回实例化的page(new_context, "测试员")
    my_page_项目经理 = 使用new_context登录并返回实例化的page(new_context, "项目经理")
    my_page_测试员.page