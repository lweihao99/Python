class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 这个方法要打印对象的姓名
    def demo(self):  # self 指向实例对象,self是一个临时的指向
        print('姓名是'+self.name)
    # 这个方法需要访问到类属性 human

    @classmethod
    def human(cls):  # cls 指向类对象,cls == Person, cls 也是一个临时指向
        print(cls.type)
    # 这个方法只需要打印 hello world

    @staticmethod
    def helloWorld():
        print('hello world')
        print(Person.type)  # 可以使用使用类对象和实例对象调用，但是会写死


# 实例对象
p1 = Person('zhangsan', 18)
p1.demo()  # 实例对象调用实例方法时，会自动将实例对象传递给self
# 使用类对象使用实例方法的时候需要手动传递实例对象给self
Person.demo(p1)

# 类方法
Person.human()

# 静态方法
Person.helloWorld()
