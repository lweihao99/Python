class Student(object):
    # 这个属性直接定义在类里，是一个元组，用来规定对象可以存在的属性
    # 想要什么属性可以使用就添加什么, 所以只有__slots__里规定的属性才能被使用
    __slots__ = ('name', 'age', 'city')

    def __init__(self, x, y):
        self.name = x
        self.age = y

    """
    函数会根据那个内存空间的调用而使self 传入那个内存空间的参数
    比如要是 s1 的内存空间调用了函数 def say_hello(self) 那么这个self.name 就是指向 zhangsan,18
    同理要是 s2 调用了函数 那么这个函数的self.name 就是 'jack'
    所以函数的self就是谁调用就指向谁
    """

    def say_hello(self):
        print("大家好，我是", self.name)


# Student('zhangsan',18)
"""代码运行逻辑
1. 调用 __new__ 方法,用来申请内存空间的
2. 在拿到了内存空间之后，调用 __init__ 方法，并让 self 指向申请好的那段内存空间
所以self.name 就是在内存空间里存储name属性名并指向x参数, self.age 同理
然后 s1 = Student('zhangsan',18); zhangsan 传给 x , 18 传给 y，而他们叫什么是由self 里面给定义的属性名来命名的

3. 让变量 s1 也指向创建好的这段内存空间

"""
s = Student('zhangsan', 18)
print("s1的名字是", s.name)
s.say_hello()

s2 = Student('jack', 21)  # 新生成一个内存空间
s2.say_hello()
# print('ox%X' % id(s1)) # 查看内存地址


print(s.name)
s.say_hello()
# print(s.height) 由于 Student 没有 height 这个属性，所以会报错==>AttributeError

# 如果直接使用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新的属性
s.city = '上海'
print(s.city)
# 如果这个属性以前存在，会修改这个属性对应的值
s.name = 'jack'
print(s.name)  # jack

# 所以python里的属性是一个动态属性，可以添加
# 那要是想要别人不能随便添加新的属性，可以使用 __slots__
