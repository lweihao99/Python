# 单例设计模式就是使对象具有唯一性

class Singleton(object):

    __instance = None  # 类属性,下划线转成私有属性
    __is_first = True  # 假设是第一次来修改这个值的话就是 True

    @classmethod
    def __new__(cls, *args, **kwargs):  # 是个类方法
        if cls.__instance is None:  # 如果变量为空就可以申请内存空间
            # 申请内存，创建一个对象，并把对象的类型设置为cls
            cls.__instance = object.__new__(cls)  # 申请内存空间

        return cls.__instance

    def __init__(self, a, b):
        # 在第一次创建对象的时候由于实例对象没有所以找类对象，由于类对象是True所以条件成立，创建对象，然后在添加实例对象False
        if self.__is_first:  # 由于实例对象优先于类对象，所以在第一次创建之后，会优先判断添加进来的实例对象就是False

            self.a = a
            self.b = b
            self.__is_first = False  # 实例对象不能修改类属性，所以这里是在内部添加了一个实例对象


"""创建对象过程
1. 调用 __new__ 方法申请内存，所以需要重写 __new__ 方法使对象不能再生成新的内存
从而使对象具有唯一性
2.如果不重写 __new__ 方法，会调用 object 的 __new__ 方法
3. object 的 __new__ 方法会申请内存
4. 如果重写了__new__ 方法，需要自己手动的申请内存
"""
s1 = Singleton('hehe', 'heiheihei')
s2 = Singleton('haha', 'xixixi')

print(s1.a == s2.a)  # True
print(s1.b == s2.b)  # True 都指向同一个地址
print(s1 is s2)  # False # 在修改了 __new__ 方法之后就变成了 True,因为都指向了同一个内存空间,s2申请不了新的内存空间
print(s1.a, s2.a)  # s2 将s1覆盖了,因为在 __new__方法之后就会运行__init__方法，而由于在同一个内存地址，所以会把之前的属性给改了
# 但是真正的单例设计模式创建出来的对象，除了第一个对象，其他后创建的对象不能覆盖之前创建的
