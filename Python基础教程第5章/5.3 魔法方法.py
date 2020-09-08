# 魔法方法，也叫魔术方法，是内里的特殊的一些方法
"""
魔法方法的特点: 
    1.不需要手动调用，会在合适的时机自动调用
    2. 这些方法都是使用 __ 开始，使用 __ 结束
    3. 方法名都是系统规定好的，在合适的时机自己调用
"""

import time
import datetime


x = datetime.datetime(2020, 2, 24, 16, 16, 45, 200)  # 是一个类
print(x)  # 调用 __str__ 方法, 更加方便
print(repr(x))  # 调用 __repr__方法, 更加精确


class Person(object):
    # 在创建对象时，会自动调用这个方法
    def __init__(self, name, age):
        print("__init__ 方法被调用了")
        self.name = name
        self.age = age

    def __del__(self):  # 在程序停止运行时,走完时会自动运行销毁
        # 当对象被销毁时，会自动调用这个方法
        print("__del__ 方法被调用了")

    def __repr__(self):
        return 'hello'

    def __str__(self):  # 直接打印对象的时候会自动调用__str__和__repr__ 方法
        return '姓名:{},年龄:{}'.format(self.name, self.age)

    def __call__(self, *args, **kwargs):  # 当对象被当做函数调用的时候就自动调用__call__方法
        print('__call__ 方法被调用了')
        # args 是一个元组，保存(1,2)
        # kwargs 是一个字典 {fn:lambda x,y:x+y}
        # args = (1, 2),kwargs = {'fn': <function <lambda> at 0x0000016DCD917280>}
        print('args = {},kwargs = {}'.format(args, kwargs))
        # 拿到字典里的 fn key, fn 的 value 是 lambda 函数，所以将这个函数赋值给fn 就等于 fn 是一个函数名
        fn = kwargs['fn']
        # 由于fn 是函数名，所以这个写法相当于 fn() # args[0]/args[1] 分别是元组里的元素 1,2
        # 而这个函数是 lambda x,y:x+y ==> 所以fn(1,2) 就是 x=1 + y=2 ==> 3
        return fn(args[0], args[1])


p = Person('zhangsan', 18)

# 如果不做任何的修改，直接打印一个对象，是文件的__name__.类型 以及内存地址,就是下面那个
# print(p)  # <__main__.Person object at 0x000002A85779C460>

# 当打印一个对象的时候，会调用这个对象的 __str__ 或者 __repr__ 方法
# 如果两个方法都写了， 会选择 __str__, 所以要二选一
# print(p)

# print(repr({'name': 'zhangsan', 'age': 18}))
# print(repr(p))
# print(p.__repr__())  # repr可以直接调用,但是魔法方法，一般不手动的调用

print(p)  # 自动调用 __str__(self)

"""使用 __str__ 和 __repr__ 方法，都会修改一个对象转化成为字符串的结果，一般来说 __str__ 方法的结果更加在意可读性，而 __repr__
方法的结果更加在意正确性(列如:datetime模块里的datetime类)(..看开头)"""

# 对象不能被直接当函数调用,但是要是使用 __call__ 方法就可以被调用了
# 对象名() ==> 调用这个对象的 p.__call__(1,2,fn=lambda x,y:x+y) 方法
n = p(1, 2, fn=lambda x, y: x+y)
print(n)  # 得到上面的结果 3
