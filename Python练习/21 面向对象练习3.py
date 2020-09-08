# 定义一个类属性，记录通过类创建了多少个对象
class Person(object):
    # 计数器
    __count = 0  # 类属性

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        x = object.__new__(cls)  # 申请内存，创建一个对象，并设置类型是 Person 类
        return x  # 需要返回才能操作内存

    def __init__(self, name, age):
        # Person.__count += 1  # 每次创建对象都会调用 __new__和__init__ 方法
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):  # 由于 __count 是类属性所以要类方法
        return cls.__count


# 每次创建对象，都会调用 __new__ 和 __init__ 方法
# 调用 __new__ 方法，使用来申请内存
# 如果不重写 __new__方法，会自动找 object 的 __new__
# object 的 __new__ 方法，默认实现是申请了一段内存，创建一个对象
p1 = Person('zhangsan', 18)
p2 = Person('lisi', 19)
p3 = Person('jack', 20)

# Perosn.__count = 100  # 如果不在前面加下划线__可以在外部修改
# print(Person.__count)
print(Person.get_count())  # 直接调用类方法


# 手动调用方法
# p4 = object.__new__(Person)  # 申请了内存，创建了一个对象，被设置它的类型是Person
# p4.__init__('tony', 23)  # 往内存传数据
# print(p4)
