import datetime
from typing import Optional, Literal


def 返回当前时间xxxx_xx_xx加N天(增加的天数: int, 格式: Optional[Literal["使用斜杠分隔符", "使用中划线分隔符", "使用datetime格式", "使用年月日格式"]] = "使用中划线分隔符"):
    if 格式 == "使用斜杠分隔符":
        return (datetime.datetime.now() + datetime.timedelta(days=增加的天数)).strftime("%Y/%m/%d")
    elif 格式 == "使用中划线分隔符":
        return (datetime.datetime.now() + datetime.timedelta(days=增加的天数)).strftime("%Y-%m-%d")
    elif 格式 == "使用datetime格式":
        return datetime.datetime.now() + datetime.timedelta(days=增加的天数)
    elif 格式 == "使用年月日格式":
        return (datetime.datetime.now() + datetime.timedelta(days=增加的天数)).strftime("%Y年%m月%d日")
    else:
        return (datetime.datetime.now() + datetime.timedelta(days=增加的天数)).strftime(str(格式))


def 返回当前时间时间戳():
    return datetime.datetime.now().timestamp()

