from playwright.sync_api import Page, expect, Browser, BrowserContext
from module import PageIns
import pytest
from filelock import FileLock
from utils.GetPath import get_path
from utils.globalMap import GlobalMap
from module import PageIns
from data_module.项目集数据类模块 import *

from allure import severity as 用例级别, step as 测试步骤, title as 用例名称, description as 用例描述
from allure_commons.types import Severity
阻塞 = Severity.BLOCKER
严重 = Severity.CRITICAL
普通 = Severity.NORMAL
不重要 = Severity.TRIVIAL
轻微 = Severity.MINOR