class Person(object):
    def __init__(self, name, age):  # self 只有在被调用的时候会指向，调用完之后就不会指向了
        self.name = name
        self.age = age

    def eat(self):  # 所以只有在调用的时候才能知道self是什么，所以函数的self跟__init__ 的self没有可比性
        print(self.name + '正在吃东西')


p1 = Person('zhangsan', 18)  # 在调用的时候回自动调用__init__ 方法，但是在调用完了之后self就谁都不指向
p2 = Person('lisi', 20)
