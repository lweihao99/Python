class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    pass


p1 = Person('zhangsan', 18)
p2 = Person('lisi', 19)

s = Student('jack', 18)

# 获取两个对象的内存地址 id(p1) == id(p2)
print(p1 is p2)  # is 身份运算符，是用来比较是否是同一个对象

# type(p1) # 其实获取的就是类对象
a = 1
if type(a) == int:
    print('a is a integer')


if type(p1) == Person:
    print('p1 is a object created by Person class')


# s 这个实例对象是否是由Student类创建的?
print(type(s) == Student)
# False,这是不对的，因为s对象是Student这个类实例化出来的，而Student是Person的子类
print(type(s) == Person)

# isinstance 用来判断一个对象是否是由指定的类(或者子类)实例化出来的,可以放多个类
print(isinstance(s, Student))  # True
print(isinstance(s, Person))  # True

print(isinstance(p1, Person))  # True
print(isinstance(p1, Student))  # False,因为 p1 不是 由Student 实例化出来的


# issubclass 用来判断一个类是否是另一个类的子类,一样可以给多个类来判断
print(issubclass(Student, Person))  # True
