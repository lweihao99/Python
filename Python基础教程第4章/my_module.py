# __all__ = ['a','test'] # 限定在[]里的才可以被调用，没有写进去的不能用
a = 'hello'


def test():
    print("hello this is itest module")


def add(a, b):
    c = a+b
    print(c)


def division(a, b):
    return a/b


_ages = 19


del (_ages)  # 不让别人用
