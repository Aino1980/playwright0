from data_module import *
from dataclasses import dataclass


@dataclass
class 项目集数据类_新建项目集(As_dict):
    项目集名称: str = "自动化创建的项目集_时间戳"
    项目集周期: str = ""
    父项目集: str = ""
    子项目集: str = ""


@dataclass
class 项目集数据类_新建项目集_temp(As_dict):
    项目集名称: str = "自动化创建的项目集_时间戳"
    项目集周期: str = ""
    父项目集: str = ""
