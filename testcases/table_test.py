from testcases import *


def test_new_context(new_context):
    my_page_测试员 = PageIns.使用new_context登录并返回实例化的page(new_context, "测试员")
    my_page_测试员.项目集.navigate()
    # index = my_page_测试员.项目集.主表格.get_header_index("开始时间")
    # loc = my_page_测试员.项目集.主表格.get_row_locator(my_page_测试员.page.get_by_text("table_test"))
    # my_page_测试员.项目集.主表格.get_cell(1, 10).text_content()
    # my_page_测试员.项目集.主表格.get_row_dict()
    my_page_测试员.项目集.主表格.get_col_list()