from playwright.sync_api import Page, expect, Playwright, BrowserContext
import pytest
import re


def test_get_by_role(page: Page, hello_world):
    """
ARIA 是Accessible Rich Internet Applications的缩写，
指可访问的富互联网应用程序。role 属性是 ARIA 中的一个重要属性，
用于定义 HTML 元素的角色，以增强网页的可访问性和可用性。
以下是一些常见的 ARIA role 属性及其解释：

• alert：表示警告信息，通常用于提示用户重要的信息或错误。

• alertdialog：表示模态弹出框，用于显示需要用户关注的信息或提示。

• application：表示应用程序，通常用于自定义的应用程序或复杂的用户界面。

• button：表示按钮，用于触发操作或执行特定的功能。

• checkbox：表示复选框，用于允许用户选择多个选项。

• combobox：表示下拉组合框，结合了输入框和下拉列表的功能。

• grid：表示网格布局，用于显示表格或类似的数据布局。

• gridcell：表示网格单元格，是 grid 角色中的子元素。

• group：表示组合框，用于将相关的元素组合在一起。

• heading：表示标题，用于定义页面或章节的标题。

• listbox：表示列表框，用于显示可选择的列表项。

• log：表示日志记录，用于显示程序或系统的日志信息。

• menu：表示菜单，用于显示一组可选择的操作或选项。

• menubar：表示菜单栏，通常位于页面顶部或侧边，包含多个菜单。

• menuitem：表示菜单项，是 menu 或 menubar 中的子元素。

• menuitemcheckbox：表示带有复选框的菜单项。

• menuitemradio：表示带有单选按钮的菜单项。

• option：表示选项，通常用于下拉列表或单选按钮组中的选项。

• presentation：表示陈述内容，用于显示只读的文本或信息。

• progressbar：表示进度条，用于显示任务或操作的进度。

• radio：表示单选按钮，用于允许用户从多个选项中选择一个。

• radiogroup：表示单选按钮组，用于将多个单选按钮组合在一起。

• region：表示区域，用于定义页面的不同部分或区域。

• row：表示表格行，用于表格布局中的行元素。

• rowgroup：表示表格行组，用于将多行组合在一起。

• scrollbar：表示滚动条，用于在内容超出显示区域时提供滚动功能。

• search：表示搜索框，用于输入搜索关键字。

• separator：表示分隔符，用于在菜单或工具栏中分隔不同的元素。

• slider：表示滑块，用于通过拖动来选择数值或范围。

• spinbutton：表示微调按钮，用于通过点击增加或减少数值。

• status：表示状态信息，用于显示当前的状态或提示。

• tab：表示选项卡，用于在多个页面或内容之间切换。

• tablist：表示选项卡列表，用于包含多个 tab 元素。

• tabpanel：表示选项卡面板，与 tab 元素配合使用，显示对应的内容。

• textbox：表示文本输入框，用于输入文本内容。

• timer：表示计时器，用于显示时间或倒计时。

• toolbar：表示工具栏，通常包含一组操作按钮或工具。

• tooltip：表示提示信息，当鼠标悬停在元素上时显示。

• tree：表示树形结构，用于显示层次化的数据。

• treegrid：表示树形表格，结合了树形结构和表格布局。

• treeitem：表示树形结构中的节点，是 tree 角色中的子元素。

这些只是 ARIA role 属性的一部分，还有其他的角色可供使用，
具体的使用场景和含义可能会因应用程序的需求而有所不同。
通过正确使用 role 属性，可以为辅助技术（如屏幕阅读器）提供更准确的信息，
帮助残障用户更好地理解和操作网页内容。
    """
    page.goto("/demo/dialog", wait_until="networkidle")
    page.get_by_text("点我开启一个dialog").click()
    expect(page.get_by_role(role="dialog")).to_be_visible()
    page.goto("/demo/checkbox", wait_until="networkidle")
    page.get_by_role("checkbox", name="开发", checked=False).set_checked(True)
    page.get_by_role("checkbox", name="开发", checked=True).set_checked(False)
    page.goto("/demo/table", wait_until="networkidle")
    expect(page.get_by_role("table")).to_be_visible()
    expect(page.get_by_role("cell")).to_have_count(13)
    expect(page.get_by_role("img", include_hidden=True)).to_have_count(4)
    page.goto("/demo/grid", wait_until="networkidle")
    expect(page.get_by_role("treegrid")).to_be_visible()
    expect(page.get_by_role("row").filter(has_text="溜达王").locator("div").nth(1)).to_have_text("44")


def test_get_by_text(page: Page):
    """
        以下规则使用条件: 参数中包含exact
        1. 规范化空白-换行转空格,前后空格忽略,多个空格作为一个空格处理
        1. 默认是包含的文本
        3. exact可以精确匹配
        4. 可以匹配正则表达式
    """
    page.goto("/demo/getbytext", wait_until="networkidle")
    expect(page.get_by_text("确定")).to_have_count(3)
    expect(page.get_by_text("确定", exact=True)).to_have_count(2)
    expect(page.get_by_text("确定 确认 肯定")).to_have_count(1)


def test_get_by_label(page: Page):
    page.goto("/demo/input", wait_until="networkidle")
    page.get_by_label("任何文字").fill("123456")
    page.get_by_label("任何文字").fill("8888888")


def test_get_by_placeholder(page: Page):
    page.goto("/demo/input", wait_until="networkidle")
    page.get_by_placeholder("不用管我,我是placeholder").fill("999999")
    page.get_by_placeholder("我是placeholder").fill("888888")


def test_get_by_title(page: Page):
    page.goto("/demo/image", wait_until="networkidle")
    expect(page.get_by_title("这是一个title")).to_be_visible()
    expect(page.get_by_title("一个title")).to_be_visible()


def test_get_by_alt_text(page: Page):
    page.goto("/demo/image", wait_until="networkidle")
    expect(page.get_by_alt_text("这是图片占位符")).to_be_visible()
    expect(page.get_by_alt_text("这是图片")).to_be_visible()


def test_get_by_test_id(page: Page, playwright:Playwright):
    page.goto("/demo/image", wait_until="networkidle")
    playwright.selectors.set_test_id_attribute("my_test_id")
    expect(page.get_by_test_id("Howls Moving Castle")).to_be_visible()


def test_get_by_locator_css(page: Page):
    page.goto("https://www.taobao.com/")
    expect(page.locator("#q")).to_be_visible()
    expect(page.locator(".image-search-icon")).to_be_visible()
    expect(page.locator(".tbh-service.J_Module")).to_be_attached()
    expect(page.locator(".tbh-service.J_Module>div>div")).to_have_count(2)
    expect(page.locator(".tbh-service.J_Module ul")).to_be_visible()
    expect(page.locator('.slick-dots[style="display: block;"]')).to_be_visible()
    expect(page.locator(".slick-dots,#q")).to_have_count(2)
    expect(page.locator('.tb-pick-feeds-container div.tb-pick-content-item a:not([data-spm="d1"])')).to_have_count(23)
    expect(page.locator('[class*="image-search-i"]')).to_be_visible()
    expect(page.locator('[class^="image-search-i"]')).to_be_visible()
    expect(page.locator('[class$="search-icon"]')).to_be_visible()


def test_get_by_locator_xpath(page: Page):
    page.goto("https://www.taobao.com/")
    expect(page.locator('//input[@id="q"]')).to_be_visible()
    expect(page.locator('//div[text()="潮电数码"]')).to_be_visible()
    expect(page.locator('//div[contains(text(),"饰时尚")]')).to_be_visible()
    expect(page.locator('//div[@data-spm-click="gostr=/tbindex.newpc.guessitem;locaid=dtab_2"][@class="tb-pick-header-tab "]')).to_be_visible()
    expect(page.locator('//div[@data-spm-click="gostr=/tbindex.newpc.guessitem;locaid=dtab_2"]|//input[@id="q"]')).to_have_count(2)
    expect(page.locator('//div[contains(@class,"service2024")]/parent::div')).to_have_count(1)
    expect(page.locator('//div[contains(@class,"service2024")]/ancestor::div')).to_have_count(2)
    expect(page.locator('//div[contains(@class,"service2024")]/following::button')).to_have_count(6)
    expect(page.locator('//li[@data-index="5"]/following-sibling::li')).to_have_count(5)
    expect(page.locator('//li[@data-index="8"]/preceding-sibling::li')).to_have_count(8)
    expect(page.locator('//li[@aria-label="查看更多"][last()-1]')).to_be_visible()


def test_filter(page: Page):
    page.goto("https://www.taobao.com/")
    assert page.locator('[aria-label="查看更多"]').filter(has_text="工业品").get_by_role("link").all_text_contents()[-1] == "定制"
    assert page.locator('[aria-label="查看更多"]').filter(has=page.locator("//a[text()='工业品']")).get_by_role("link").all_text_contents()[-1] == "定制"
    expect(page.locator('[aria-label="查看更多"]').filter(has_text="工业品").filter(has_not_text="定制")).to_have_count(0)


def test_and_or_visible(page: Page):
    page.goto("https://www.taobao.com/")
    expect(page.get_by_text("电脑").and_(page.get_by_role("link"))).to_be_visible()
    expect(page.get_by_text("电脑").and_(page.get_by_role("link")).or_(page.locator("#q"))).to_have_count(2)
    expect(page.get_by_text("电脑").locator("visible=true")).to_be_visible()


def test_nth_all(page: Page):
    page.goto("https://www.taobao.com/")
    expect(page.locator('[aria-label="查看更多"]').last).to_contain_text("鲜花")
    expect(page.locator('[aria-label="查看更多"]').first).to_contain_text("电脑")
    expect(page.locator('[aria-label="查看更多"]').nth(4)).to_contain_text("男装")
    for _ in page.locator('[aria-label="查看更多"]').all():
        print(_.text_content())


def test_frame_locator(page: Page):
    page.goto("http://www.自动化测试.com/demo/iframe", wait_until="networkidle")
    baidu = page.frame(url='https://www.baidu.com/')
    baidu.fill("#kw", "playwright")
    page.frame_locator('[src="http://www.自动化测试.com"]').get_by_text("B站视频").click()














