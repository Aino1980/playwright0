class Human:

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.birthday = 2024-age

    def run(self):
        print(f"{self.name}跑起来了")

    def job(self):
        if self.age < 35:
            print(f"{self.name}还能找到工作")
        else:
            print(f"{self.name}已经不好找工作了")


class Tester(Human):
    def __init__(self, name, sex, age, tech):
        super().__init__(name, sex, age)
        self.tech = tech

    def skill(self):
        print(f"{self.name}会{self.tech}")


if __name__ == "__main__":
    zhang3 = Human("zhangsan", "man", 28)
    zhang3.run()
    zhang3.job()

    liudawang = Tester("liudawang", "man", 44, "playwright")
    liudawang.run()
    liudawang.job()
    liudawang.skill()

