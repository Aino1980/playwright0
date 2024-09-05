
from testcases import *


def test_table(new_context):
    my_page_测试员 = PageIns.使用new_context登录并返回实例化的page(new_context, "测试员")
    my_page_测试员.项目集.navigate()
    index = my_page_测试员.项目集.主表格.get_header_index("开始时间")
    print(index)
    loc = my_page_测试员.项目集.主表格.get_row_locator(my_page_测试员.page.get_by_text("table_test"))
    print(loc.text_content())
    print(my_page_测试员.项目集.主表格.get_cell(0, -1).text_content())
    print(my_page_测试员.项目集.主表格.get_row_dict(5)["项目集名称"])

