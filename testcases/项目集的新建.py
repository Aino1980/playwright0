from testcases import *


def test_项目集的新建(new_context, 删除项目集):
    my_page_测试员 = 使用new_context登录并返回实例化的page(new_context, "测试员")
    my_page_测试员.项目集.创建项目集()


@pytest.fixture
def 删除项目集(new_context):
    yield
    my_page_测试员 = 使用new_context登录并返回实例化的page(new_context, "测试员")
    my_page_测试员.项目集.删除项目集("自动化创建项目集")
