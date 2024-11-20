from module import *
from module.table import Table
from module.locators import Locators
from utils.my_date import *
import allure


class PageObject:
    def __init__(self, page: Page):
        self.page = page
        self.url = ""
        self.locators = Locators(self.page)

    def navigate(self):
        self.page.goto(self.url)

    def table(self, 唯一文字, 表格序号=-1):
        return Table(self.page, 唯一文字, 表格序号)

    def click_button(self, button_name, timeout=30_000, nth=-1):
        button_loc = self.page.locator("button")
        for 单字符 in button_name:
            button_loc = button_loc.filter(has_text=单字符)
        button_loc.nth(nth).click(timeout=timeout)

    def search(self, 搜索内容: str, placeholder=None):
        if placeholder:
            self.page.locator(f"//span[@class='ant-input-affix-wrapper']//input[contains(@placeholder,'{placeholder}')]").fill(搜索内容)
        else:
            self.page.locator(".ant-input-affix-wrapper input").fill(搜索内容)
        self.page.wait_for_load_state("networkidle")

    def hover_retry(self, hover对象: Locator, 下一步点击对象: Locator, 第一步动作="hover", 第二步动作="click", timeout=30_000):
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout / 1000:
                pytest.fail(f"hover重试{hover对象.__str__()}在{timeout / 1000}秒内未成功")
            try:
                self.page.mouse.move(x=1, y=1)
                self.page.wait_for_timeout(1_000)
                if 第一步动作 == "hover":
                    hover对象.last.hover()
                else:
                    hover对象.last.click()
                self.page.wait_for_timeout(3_000)
                if 第二步动作 == "click":
                    下一步点击对象.last.click(timeout=3000)
                else:
                    下一步点击对象.last.wait_for(state="visible", timeout=3000)
                break
            except:
                continue

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

    def 表单_日期(self, 表单项名称: str, 日期: str, 表单最上层定位: Locator = None, timeout: float = None):
        if 表单最上层定位:
            日期控件定位 = 表单最上层定位.locator(self.locators.表单项中包含操作元素的最上级div(表单项名称))
        else:
            日期控件定位 = self.locators.表单项中包含操作元素的最上级div(表单项名称)
        日期列表 = 日期.split(",")
        for index, 单日期 in enumerate(日期列表):
            try:
                int(单日期)
                格式化后的日期 = 返回当前时间xxxx_xx_xx加N天(int(单日期))
            except:
                格式化后的日期 = 单日期
            日期控件定位.locator("input").nth(index).click(timeout=timeout)
            日期控件定位.locator("input").nth(index).fill(格式化后的日期, timeout=timeout)
            日期控件定位.locator("input").nth(index).blur(timeout=timeout)

    def 快捷操作_填写表单(self, 表单最上层定位: Locator = None, timeout=None, **kwargs):
        for 表单项, 内容 in kwargs.items():
            if not 内容:
                continue
            elif self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-input").count():
                self.表单_文本框填写(表单项名称=表单项, 需要填写的文本=内容, 表单最上层定位=表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-select-selector").count():
                self.表单_下拉框选择(表单项名称=表单项, 需要选择的项=内容, 表单最上层定位=表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-radio-group").count():
                self.表单_radio选择(表单项名称=表单项, 需要选择的项=内容, 表单最上层定位=表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).get_by_role("switch").count():
                self.表单_switch开关(表单项名称=表单项, 开关状态=内容, 表单最上层定位=表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-picker").count():
                self.表单_日期(表单项名称=表单项, 日期=内容, 表单最上层定位=表单最上层定位, timeout=timeout)
            else:
                pytest.fail(f"不支持的快捷表单填写:\n{表单项}:{内容}")

    def 快捷操作_填写表单_增加根据数据类确定唯一表单版(self, 表单最上层定位: Locator = None, timeout=None, **kwargs):
        页面上已有的表单项列表 = []
        已经有唯一表单项 = False
        if 表单最上层定位:
            处理后的表单最上层定位 = 表单最上层定位
        else:
            for index, 表单项 in enumerate(kwargs.keys()):
                if index == 0:
                    try:
                        self.locators.表单项中包含操作元素的最上级div(表单项).last.wait_for(timeout=timeout)
                    except:
                        pass

                if self.locators.表单项中包含操作元素的最上级div(表单项).count() == 0:
                    continue
                else:
                    if self.locators.表单项中包含操作元素的最上级div(表单项).count() == 1:
                        已经有唯一表单项 = True
                    页面上已有的表单项列表.append(self.locators.表单项中包含操作元素的最上级div(表单项))
                if 已经有唯一表单项 and len(页面上已有的表单项列表) >= 2:
                    break

            包含可见表单项的loc = self.page.locator("*")
            for 已有表单项_loc in 页面上已有的表单项列表:
                包含可见表单项的loc = 包含可见表单项的loc.filter(has=已有表单项_loc)
            if 已经有唯一表单项:
                处理后的表单最上层定位 = 包含可见表单项的loc.last
            else:
                处理后的表单最上层定位 = min(包含可见表单项的loc.all(), key=lambda loc: len(loc.text_content()))

        for 表单项, 内容 in kwargs.items():
            if not 内容:
                continue
            if self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-input").count():
                self.表单_文本框填写(表单项名称=表单项, 需要填写的文本=内容, 表单最上层定位=处理后的表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-select-selector").count():
                self.表单_下拉框选择(表单项名称=表单项, 需要选择的项=内容, 表单最上层定位=处理后的表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-radio-group").count():
                self.表单_radio选择(表单项名称=表单项, 需要选择的项=内容, 表单最上层定位=处理后的表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).get_by_role("switch").count():
                self.表单_switch开关(表单项名称=表单项, 开关状态=内容, 表单最上层定位=处理后的表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-picker").count():
                self.表单_日期(表单项名称=表单项, 日期=内容, 表单最上层定位=处理后的表单最上层定位, timeout=timeout)
            else:
                pytest.fail(f"不支持的快捷表单填写:\n{表单项}:{内容}")

    @allure.step("重试")
    def 重试(self, *args, 重试次数=10):
        """
        重试一系列步骤
        @param args:
        1. 第一个传的是子步骤的指针,比如locator.click, locator.hover
        2. 如果只传子步骤指针,则默认执行时的timeout为3_000
        3. 如果需要传参,则需要使用(子步骤指针, 位置参数1, 位置参数2, {"命名参数名称1": 命名参数值1, "命名参数名称2": 命名参数值2})
        @param 重试次数:
        @return:
        """
        for _ in range(重试次数):
            try:
                for arg in args:
                    if isinstance(arg, tuple):
                        with allure.step(f"{arg[0].__name__} 参数:{arg[1:]}"):
                            func = arg[0]
                            param = arg[1:]
                            named_params = {}
                            positional_params = []
                            for in_param in param:
                                if isinstance(in_param, dict):
                                    named_params.update(in_param)
                                else:
                                    positional_params.append(in_param)
                            func(*positional_params, **named_params)
                    else:
                        with allure.step(arg.__name__):
                            arg(timeout=3000)
                break
            except Exception as e:
                if _ == 重试次数 - 1:
                    print(f"已经重试{重试次数}次，但仍然失败，错误信息：", e)
                    raise e
        # for _ in range(重试次数):
        #     try:å
        #         for arg in args:
        #             if isinstance(arg, tuple):
        #                 with allure.step(f"{arg[0].__name__} 参数:{arg[1:]}"):
        #                     f = arg[0]
        #                     param = arg[1:]
        #                     f(*param)
        #             else:
        #                 with allure.step(arg.__name__):
        #                     arg(timeout=3000)
        #         break
        #     except Exception as e:
        #         if _ == 重试次数 - 1:
        #             print(f"已经重试{重试次数}次，但仍然失败，错误信息：", e)
        #             raise e
