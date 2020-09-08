class Person(object):
    """
    这是一个人类
    """
    __slots__ = ('name', 'age')  # 限定属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃放')


# 'name':''zhangsan' name属性对应一个字符串, "age":18 age属性对应数字, "eat":<function> 也可以被当做属性对应一个函数
p = Person('zhangsan', 18)
print(dir(p))  # 列举对象支持的所有属性和方法 其中就有 'age' 'eat' 'name'
print(p.__class__)  # 告诉你是什么类 <class '__main__.Person'>
print(p.__dict__)  # 把对象属性和值转化成为一个字典 {'name': 'zhangsan', 'age': 18}
# print(p.__dir__()) ## 等价于 dir(p)
print(p.__doc__)  # 文档说明，说明内容 对象名.__doc__
print(Person.__doc__)  # 类名.__doc__
print(p.__module__)  # 直接运行就是 __main__
