class Calculator(object):

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b


# 直接用类名来调用静态方法
Calculator.add(1, 3)
print(Calculator.minus(3, 1))
# 本来需要创建一个对象来调用
# c = Calculator() # 这里由于完全不需要传递属性所以不需要创建对象
# c.add(1,2)


class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):  # 对象方法有一个参数self,指的是实例对象
        print(self.name+'正在吃'+food)

    # 如果一个方法里没有用到实例对象的任何属性，可以将这个方法转成 static
    @staticmethod  # 静态方法
    def demo():  # 默认的方法都是对象方法 def demo(self):
        print('hello')

    @classmethod
    def test(cls):  # 如果这个函数用到了类属性,我们可以定义成为一个类方法
        # 类方法会有一个参数cls, 也不需要手动传参，会自动传参
        # cls 指的是类对象 cls == Person ==> True
        print(cls.type)  # cls is Person
        print('yes')


p1 = Person('zhangsan', 18)

p2 = Person('lisi', 19)

# <bound method Person.eat of <__main__.Person object at 0x000001B97F2D4C10>>
# print(p1.eat)

# <bound method Person.eat of <__main__.Person object at 0x000001B97F34C340>>
# print(p2.eat)  # 跟p1.eat 地址不一样

# print(Person.eat)  # <function Person.eat at 0x000001BC7E470790>

# 实例对象在调用方法时，不需要给形参self传参，会自动的把实例对象传递给self
# 所以这里 p.eat() 的 p 会自动传给 eat() 的 self
# eat 是对象方法，可以直接使用实例对象.方法名(参数) 调用
# 使用对象名.方法名(参数) 调用的方式，不需要传递self
# 会自动将对象名传递给self
p1.eat('红烧牛肉面')  # 直接使用实例对象调用方法


# TypeError: eat() missing 1 required positional argument: 'food'
# Person.eat("西红柿炒蛋")

# 对象方法还可以使用 类对象来调用
# 类名.方法名(参数) 不会自动给self 传参，需要手动指定self
Person.eat(p2, '西红柿炒蛋')


# 静态方法, 没有用到实例对象的任何属性
Person.demo()  # 可以直接调用
p1.demo()


# 类方法: 可以使用实例对象和类对象来调用
p1.test()
Person.test()

"""
对象方法或者实例方法，一般情况下会用到实例对象的属性，self指向调用这个方法的实例对象.
有两种调用方式: 
1. 实例对象.方法名 ==> 不需要手动给self传参,会自动将实例对象传递给 self, 比如: p1.eat('value')
2. 类对象.方法名 ==> 需要手动的给 self 传参, 比如: Person.eat(p1,'value')
"""
"""
类方法:会有一个参数叫 cls, 这个cls指向的是类对象
如果一个方法只使用到类属性，可以将这个方法定义为类方法
"""
"""
静态方法==>即用不到类对象属性，实例对象的属性,感觉就像和这个类没有关系一样，这就可以把这个定义为静态方法
"""
