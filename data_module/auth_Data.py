class MyData:
    def __init__(self, local=True, excel=None, yaml=None, feishu=None):
        self.local = local
        self.excel = excel
        self.yaml = yaml
        self.feishu = feishu

    def userinfo(self, 被测环境, 角色名称):
        user = ""
        if self.excel:
            pass
            # todo 把excel转换成字典的方法
        elif self.yaml:
            pass
            # todo 把yaml转换成字典的方法
        elif self.feishu:
            pass
            # todo 把feishu转换成字典的方法
        else:
            user = {"playwright":
                        {"测试员":
                             {"username": "winni", "password": "playwright001"},
                         "项目经理":
                             {"username": "zhang20121104", "password": "playwright123"}},
                    "playwright0":
                        {"测试员":
                             {"username": "winni1", "password": "playwright001"},
                         "项目经理":
                             {"username": "tracy2012", "password": "playwright123"}},
                    }

        return user[被测环境][角色名称]