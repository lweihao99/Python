# 一 创建一个类People,拥有的方法为砍柴,娶媳妇,回家;实例化对象,执行相应的方法
"""
显示如下:
    李四,18岁,男,开车去娶媳妇
    张三,22岁,男,上山去砍柴
    王麻子,10岁,女,辍学回家
"""


class People(object):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 砍柴方法
    def choop_wood(self):
        print("{},{}岁,{},上山去砍柴".format(self.name, self.age, self.gender))

    # 开车去娶媳妇
    def drive_car(self):
        print("{},{}岁,{},开车去娶媳妇".format(self.name, self.age, self.gender))

    # 辍学回家
    def drop_out(self):
        print("{},{}岁,{},辍学回家".format(self.name, self.age, self.gender))


p1 = People('李四', 18, '男')
p2 = People('张三', 22, '男')
p3 = People('王麻子', 10, '女')

p2.choop_wood()
p1.drive_car()
p3.drop_out()
