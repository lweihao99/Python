class Animal(object):  # 由于重复的代码很多，所以可以将这个Animal类设置为父类，其他为子类，这样子类就可以继承重复的方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name+' is sleeping')


class Dog(Animal):  # 在括号里写父类也就是Animal
    # def __init__(self, name, age): # 这些代码父类里有所以可以直接删除掉
    #     self.name = name
    #     self.age = age

    # def sleep(self):
    #     print(self.name+'is sleeping')

    def bark(self):
        print(self.name + ' is barking')


class Student(Animal):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    # def sleep(self):
    #     print(self.name+'is sleeping')

    def study(self):
        print(self.name + ' is studing as well')


# 由于Dog()先调用 __new__ 方法，在调用 __init__方法
# Dog 里没有 __new__方法，所以会查看父类里是否重写了 __new__ 方法
# 父类由于也没有重写 __new__ 方法，所以会查找父类的父类，也就是 object，而object里有

# Dog里没有 __init__ 方法 ==> 调用父类的 __init__ 方法
dog = Dog('puffy', 3)
print(dog.name, dog.age)  # 父类里定义的属性，子类可以直接使用
dog.sleep()  # 父类的方法可以直接调用
dog.bark()


student = Student('jack', 18)
student.sleep()
student.study()
# 注意子类不能调用其他的子类的方法,子类之间是没有任何关系
