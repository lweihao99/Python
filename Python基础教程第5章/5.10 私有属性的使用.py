import datetime


class Person(object):

    def __init__(self, name, age):

        self.name = name
        self.age = age
        self.__money = 1000  # 以两个下划线开始的变量是私有变量, 不能够直接获取

    # def test(self):
    #     self.__money += 10  # 在这里可以访问到私有属性,可以内部访问

    def get_money(self):
        # 只要调用这个方法就能记录下来
        print("{}查询了余额".format(datetime.datetime.now()))
        return self.__money

    def set_money(self, money):
        if type(money) != int:
            print("设置的余额不合法")
            return
        print("修改了余额")
        self.__money = money

    def __demo(self):  # 以两个下划线开始的函数，是私有函数，在外部是不能被调用的
        print("我是demo函数, name={}".format(self.name))

    def test(self):
        self.__demo()  # 只能在内部使用


p1 = Person('zhangsan', 18)

print(hex(id(p1)))  # hex 将integer number转化成16进制

print(p1.name)
print(p1.age)  # 这种变量可以直接获取
# print(p.__money) # 不能够直接获取

# p1.test()

# 获取私有变量的方式:
# 1. 使用 对象._类名__私有变量名获取
# print(p1._Person__money)  # 通过这种方式也能获取到私有属性

# 2. 定义get 和 set 方法来获取, 接口函数
print(p1.get_money())  # 通过接口函数来获取到私有属性

p1.set_money(2000)  # 修改私有属性
print(p1.get_money())

# 3. 使用 property 来获取(以后补充)


# 强行获取私有函数
# p1._Person__demo()
