class A(object):
    def demo_a(self):
        print('im the demo func in the class A')


class B(object):
    def demo_b(self):
        print('im demo func in the class B')

    def foo(self):
        print('im foo in the class B')

# 在 Python里允许多继承


class C(A):  # 如果不写父类，Python3以后，默认继承自object
    def foo(self):
        print('im foo in the class C')


class D(B):
    pass


class X(D, C):  # 这里的顺序是先D后C，同理要是反之就是先C后D，就是继承的顺序会影响到__mro__
    pass


c = C()
c.demo_a()

# 如果两个不同的父类有同名方法,有一个类属性可以查看方法的调用顺序 就是__mro__方法
c.foo()
# 继承传递的概念
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C.__mro__)  # 先找C==>A==>B==>object 如果这些类里都没有，那么就会报错

# 查找顺序是深度优先
x = X()
x.foo()
print(X.__mro__)  # (<class '__main__.X'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# 先在D类的那条线查找，如果没有再去C类那条线,这就是深度优先，查找顺序受继承顺序影响
