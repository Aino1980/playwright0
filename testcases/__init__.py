from playwright.sync_api import Page, expect, Browser, BrowserContext
from module.PageInstance import PageIns
import pytest
from filelock import FileLock
from utils.GetPath import get_path
from utils.globalMap import GlobalMap
from module.BasePage import 使用new_context登录并返回实例化的page