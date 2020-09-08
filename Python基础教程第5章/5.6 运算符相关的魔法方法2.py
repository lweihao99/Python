class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, value):  # 这里self 指向 p1, value 指向 p2, 因为传参
        return self.name == value.name and self.age == value.age

    # def __ne__(self, value): # 使用 != 运算符会自动调用这个方法
    #     return

    def __gt__(self, value):  # greater then 使用 > 会自动调用这个方法
        return self.age > value.age

    def __ge__(self, value):  # greater equal 使用 >= 运算符会自动调用
        return super().__ge__(value)

    # def __lt__(self, value):  # less then 使用 < 运算符会自动调用
        # return super().__lt__(value)

    # def __le__(self, value):  # less equal 使用<= 运算符会自动调用
        # return super().__le__(value)

    def __add__(self, value):  # 使用 + 运算符会自动调用, 注意这些运算符没有对应的方法不能执行，会报错
        return self.age + value.age

    def __sub__(self, value):  # 使用 - 运算符会自动调用, 注意调用的时候的参数传入，不对的话会报错
        return self.age - value.age

    def __mul__(self, value):  # *
        return self.name * value

    def __truediv__(self, value):  # /
        return self.age / value

    def __pow__(self, value):  # 幂运算
        return self.age ** value

    def __str__(self):  # 类型转换由于是将数据转换成为字符串所以会自动调用这个方法
        return 'hello'

    def __int__(self):  # 类型转换成为 int 会调用这个方法
        return 20

    def __float__(self):  # 转换成为 float 会自动调用这个方法
        return 3.14


p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)
p3 = Person('lisi', 19)
print(p1 is p2)  # False

# == 运算符本质其实是调用对象的 __eq__ 方法， 获取 __eq__ 方法的返回结果
# a == b => a.__eq__(b)
print(p1 == p2)  # 可以在 __eq__ 改变运算方法

# 。 != 本质是调用 __ne__ 方法，或者 __eq__ 方法取反
print(p1 != p2)  # 优先调用 __ne__ 如果没有就 __eq__ 方法取反


print(p1 > p3)  # 如果没有写对应的方法是不能比较的,不然会报错


print(p1 + p2)
print(p1 - p2)  # 比较的方法，取决于你如何写方法

print(p1 * 10)
print(p1 / 2)
print(p1 ** 2)

# python 内置类,一些底层的运行逻辑和思想
# str() 将对象转换成为字符串，会自动调用 __str__ 方法
# 1. str() 转换会调用 __str__ 2. 直接打印对象也会调用__str__
print(str(p1))  # 转换成为字符串, 默认会转换成为类型 + 内存地址

# int() ==> 调用对象的 __int__ 方法
print(int(p1))

# float() 转换会调用 __float__ 方法
print(float(p1))

# 系统自带的重写了比较规则，而使用类的对象系统会默认比较内存地址
num1 = [1, 2, 3]
num2 = [1, 2, 3]
print(num1 == num2)
