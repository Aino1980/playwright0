from module import *


class 项目集_类(PageObject):
    def __init__(self, page):
        super().__init__(page)
        self.url = "/portfolio"
        self.项目集名称 = self.page.get_by_placeholder("1-32个字符")
        self.请输入项目集名称 = self.page.get_by_placeholder("请输入项目集名称")
        self.设置齿轮 = self.page.locator('//span[@aria-label="setting"]').locator("xpath=/..")
        self.运维操作 = self.page.get_by_text("运维操作")
        self.暂无数据 = self.page.get_by_text("暂无数据")

    @property
    def 主表格(self):
        return self.table("项目集名称")

    def 创建项目集(self, 项目集名称="自动化创建项目集", 是否需要纳秒时间戳=True):
        self.navigate()
        self.click_button("新建", timeout=3_000)
        if 是否需要纳秒时间戳:
            项目集名称 = f"{项目集名称}_{time.time_ns()}"
        self.项目集名称.fill(项目集名称)
        self.click_button("确定")
        self.请输入项目集名称.fill(项目集名称)
        expect(self.page.locator("a").filter(has_text=项目集名称)).to_be_visible()
        return 项目集名称

    def 删除项目集(self, 项目集名称):
        while True:
            self.navigate()
            # self.请输入项目集名称.fill(项目集名称)
            self.search(项目集名称, "请输入项目集名称")
            if self.暂无数据.count():
                break
            else:
                self.设置齿轮.last.click()
                self.运维操作.click()
                self.click_button("删除项目集")
                self.click_button("确定")




