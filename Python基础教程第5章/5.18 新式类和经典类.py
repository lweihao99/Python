# 括号里面是指定父类
class Person(object):  # 指定 Person 继承自 object
    pass


class Student:  # 后面的object可以不写,这里没有指定父类，Python3默认继承object
    pass

# 新式类和经典类的概念:
# 1.新式类：继承自object的类，我们称之为新式类
# 2.经典类：不继承自object的类


# 区别在Python2里，如果不手动指定一个类的父类是object，这个类就是一个经典类
p = Person()
s = Student()
print(dir(p))
print(dir(s))

# 在Python3里没有经典类，都是新式类
