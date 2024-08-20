from module import *
from module.table import Table
from module.locators import Locators


class PageObject:
    def __init__(self, page: Page):
        self.page = page
        self.url = ""
        self.locators = Locators(self.page)

    def navigate(self):
        self.page.goto(self.url)

    def table(self, 唯一文字, 表格序号=-1):
        return Table(self.page, 唯一文字, 表格序号)

    def click_button(self, button_name, timeout=30_000):
        button_loc = self.page.locator("button")
        for 单字符 in button_name:
            button_loc = button_loc.filter(has_text=单字符)
        button_loc.click(timeout=timeout)

    def search(self, 搜索内容: str, placeholder=None):
        if placeholder:
            self.page.locator(f"//span[@class='ant-input-affix-wrapper']//input[contains(@placeholder,'{placeholder}')]").fill(搜索内容)
        else:
            self.page.locator(".ant-input-affix-wrapper input").fill(搜索内容)
        self.page.wait_for_load_state("networkidle")

    def 表单_文本框填写(self, 表单项名称: str, 需要填写的文本: str, 表单最上层定位: Locator = None, timeout: float = None):
        if 表单最上层定位:
            表单最上层定位.locator(self.locators.表单项中包含操作元素的最上级div(表单项名称)).locator("input,textarea").locator("visible=true").last.fill(需要填写的文本, timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(表单项名称).locator("input,textarea").locator("visible=true").last.fill(需要填写的文本, timeout=timeout)

    def 表单_下拉框选择(self, 表单项名称: str, 需要选择的项: str, 表单最上层定位: Locator = None, timeout: float = None):
        if 表单最上层定位:
            表单最上层定位.locator(self.locators.表单项中包含操作元素的最上级div(表单项名称)).locator("visible=true").click(timeout=timeout)
            if 表单最上层定位.locator(self.locators.表单项中包含操作元素的最上级div(表单项名称)).locator('//input[@type="search"]').count():
                表单最上层定位.locator(self.locators.表单项中包含操作元素的最上级div(表单项名称)).locator('//input[@type="search"]').fill(需要选择的项, timeout=timeout)
            self.page.locator(".ant-select-dropdown").locator("visible=true").get_by_text(需要选择的项).click(timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(表单项名称).locator("visible=true").click(timeout=timeout)
            if self.locators.表单项中包含操作元素的最上级div(表单项名称).locator('//input[@type="search"]').count():
                self.locators.表单项中包含操作元素的最上级div(表单项名称).locator('//input[@type="search"]').fill(需要选择的项, timeout=timeout)
            self.page.locator(".ant-select-dropdown").locator("visible=true").get_by_text(需要选择的项).click(timeout=timeout)
        expect(self.page.locator(".ant-select-dropdown")).to_be_hidden(timeout=timeout)

    def 表单_radio选择(self, 表单项名称: str, 需要选择的项: str, 表单最上层定位: Locator = None, timeout: float = None):
        if 表单最上层定位:
            表单最上层定位.locator(self.locators.表单项中包含操作元素的最上级div(表单项名称)).locator("label").locator("visible=true").filter(has_text=需要选择的项).locator("input").check(timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(表单项名称).locator("label").locator("visible=true").filter(has_text=需要选择的项).locator("input").check(timeout=timeout)

    def 表单_switch开关(self, 表单项名称: str, 开关状态: str, 表单最上层定位: Locator = None, timeout: float = None):
        if "开" in 开关状态 or "是" in 开关状态:
            开关状态bool = True
        else:
            开关状态bool = False
        if 表单最上层定位:
            表单最上层定位.locator(self.locators.表单项中包含操作元素的最上级div(表单项名称)).get_by_role("switch").set_checked(开关状态bool, timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(表单项名称).get_by_role("switch").set_checked(开关状态bool, timeout=timeout)