# 写一个计算器类，实现加减乘除
class Calculator:

    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def diff(a, b):
        return a-b

    @staticmethod
    def mult(a, b):
        return a*b

    @staticmethod
    def divide(a, b):
        return a / b


print(Calculator.add(12, 8))
print(Calculator.diff(16, 12))
print(Calculator.mult(2, 2))
print(Calculator.divide(6, 3))


# 创建一个Person类，统计Person类的对象的个数
class Person:
    __count = 0

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        x = object.__new__(cls)
        return x

    def __init__(self, name, age):
        # Person.count += 1
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):
        return cls.__count


p1 = Person('jack', 19)
p2 = Person('lina', 20)
p3 = Person('lisa', 17)

print('Person类创建了{}个对象'.format(Person.get_count()))
