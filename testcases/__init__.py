from playwright.sync_api import Page, expect, Browser, BrowserContext
from module.PageInstance import PageIns
import pytest
from filelock import FileLock
from utils.GetPath import get_path