# 继承特点:如果一个类A继承自类B,由类A创建出来的实例对象,都能直接使用类B里定义的方法


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name, 'is sleeping')


class Student(Person):
    def __init__(self, name, age, school):
        # self.name = name
        # self.age = age
        # 子类在父类实现的基础上，又添加了自己的新的功能
        # 可以调用父类方法来实现
        # 1.init是对象方法，所以 父类名.方法名(self,参数列表) # 手动调用需要手动传参所以self必须要写
        # Person.__init__(self, name, age)
        # 2. 使用 super,直接调用父类的方法，推荐使用第二种
        super(Student, self).__init__(name, age)
        self.school = school

    def sleep(self):  # 重写父类方法
        print(self.name, 'is sleeping during the breaktime')

    def study(self):
        print(self.name, 'is studing')


s = Student('jerry', 18, 'harvord')  # 调用了父类的__init__方法
s.sleep()  # 调用了父类的 sleep 方法

print(Student.__mro__)  # mro = method resolution object


# 1.子类的实现和父类的实现完全不一样，子类可以选择重写父类的方法
# 2.子类在父类的基础上又有更多的实现,
# 就是有更多的需求,需要先调用一下父类的方法传参，在添加需要的新的属性
