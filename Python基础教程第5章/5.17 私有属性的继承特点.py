

class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eat(self):
        print(self.name + ' is eating')

    def __test(self):
        print('im __test func in the Animal class')


class Person(Animal):
    # 装饰器如果父类有的话可以省略
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(cls)

    def __demo(self):
        print('im private method')


p = Person('zhangsan', 18)
print(p.name)
p._Person__demo()  # 调用Person里的私有方法,这是自己类里定义的私有方法 object._class__Method()
# p._Person__test() # 父类私有属性不能被子类继承
p._Animal__test()  # 可以通过 对象名._父类名__私有属性() 调用

# 结论:父类的私有属性和方法，子类不会继承
