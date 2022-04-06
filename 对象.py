# 类方法
class Car1(object):
    name = 'BMW'

    def __init__(self, name):
        self.name = name

    @classmethod
    def run(cls, speed):
        print(cls.name, speed, '行驶')


# 静态方法
class Car2(object):
    name = 'Benz'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def run(speed):
        print(Car2.name, speed, '行驶')


# 实例方法
class Car3(object):
    name = 'Audi'

    def __init__(self, name):
        self.name = name

    def run(self, speed):
        print(self.name, speed, '行驶')


c1 = Car1("宝马")
c2 = Car2("奔驰")
c3 = Car3("奥迪")
c1.run("100")#类方法不能访问实例变量
c2.run("110")#静态方法不能访问类和实例变量
Car1.run("120")#类方法不需要实例
Car2.run("130")#静态方法不需要实例
c3.run("150")#实例方法可以访问实例参数和类参数
