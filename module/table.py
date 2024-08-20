from module import *


class Table:
    def __init__(self, page: Page, 唯一文字: str, 表格序号: int = -1):
        self.page = page
        self.page.wait_for_load_state("networkidle")
        self.table_div = self.page.locator(".ant-table-wrapper").filter(has_text=唯一文字).nth(表格序号)
        self.table_header_tr = self.table_div.locator("//thead/tr")

    def get_header_index(self, 表头文字: str) -> int:
        return self.table_header_tr.locator("th").all_text_contents().index(表头文字)

    def get_row_locator(self, 行元素定位: Locator) -> Locator:
        return self.table_div.locator("tr").filter(has=行元素定位)

    def get_cell(self, 表头文字or列序号: str | int, 行元素定位or行序号or行文字: Locator | int | str) -> Locator:
        if isinstance(表头文字or列序号, str):
            列序号 = self.get_header_index(表头文字or列序号)
        else:
            列序号 = 表头文字or列序号

        if isinstance(行元素定位or行序号or行文字, Locator):
            行定位 = self.get_row_locator(行元素定位or行序号or行文字)
        elif isinstance(行元素定位or行序号or行文字, str):
            行定位 = self.table_div.locator("tr").filter(has_text=行元素定位or行序号or行文字)
        else:
            行定位 = self.table_div.locator("tbody").locator('//tr[not(@aria-hidden="true")]').nth(行元素定位or行序号or行文字)

        return 行定位.locator("td").nth(列序号)

    def get_row_dict(self, 行元素定位or行序号: Locator | int = "random") -> dict:
        if isinstance(行元素定位or行序号, int):
            tr = self.table_div.locator("tbody").locator("tr").locator("visible=true").nth(行元素定位or行序号)
        elif isinstance(行元素定位or行序号, Locator):
            tr = self.table_div.locator("tr").filter(has=行元素定位or行序号)
        else:
            all_tr = self.table_div.locator("tbody").locator("tr").locator("visible=ture").all()
            tr = random.choice(all_tr)

        td_text_list = tr.locator("td").all_text_contents()
        header_text_list = self.table_header_tr.locator("th").all_text_contents()
        row_dict = dict(zip(header_text_list, td_text_list))
        return row_dict

    def get_col_list(self, 表头文字: str) -> list:
        index = self.get_header_index(表头文字)
        all_tr = self.table_div.locator("tbody").locator("tr").locator("visible=true").all()
        col_list = []
        for tr in all_tr:
            col_list.append(tr.locator("td").nth(index).text_content())
        return col_list


