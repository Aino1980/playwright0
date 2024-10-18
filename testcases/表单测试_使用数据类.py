import random

from testcases import *


def test_表单测试_使用数据类(new_context):
    with 测试步骤("尝试登录并跳转"):
        my_page_测试员 = PageIns.使用new_context登录并返回实例化的page(new_context, "测试员")
        my_page_测试员.项目集.navigate()
    with 测试步骤("填写项目集内容"):
        my_page_测试员.项目集.click_button("新建")
        新建项目 = 项目集数据类_新建项目集(项目集名称="test123", 项目集周期="0,365", 父项目集="公共项目集")
        my_page_测试员.项目集.快捷操作_填写表单(**新建项目.as_dict())
    assert random.choice([True, False])