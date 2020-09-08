class Person(object):
    type = '人类'  # 这个属性定义在类里，函数(方法)之外，我们称之为 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 对象 p 是通过 Person 类 创建出来的实例对象
p1 = Person('zhangsan', 18)
p2 = Person('lisi', 19)

print('0x%x' % (id(Person)))  # 0x221d1865dd0
# Person 类 也有一个内存地址,就是创建对象的模板也保存在内存里面

# p1 和 p2 是实例对象 而 Person 是类对象
# 只要创建了一个实例对象，这个实例对象就有自己的name和age属性,就是每个实例对象的内存空间里都保存了相对应属性
# 而这种属性被称之为 对象属性，即每个实例对象都保存的属性
# 对象属性 name 和 age 实在 __init__ 方法里定义的
# 每个实例对象之间的属性没有关联，互不影响


x = p1  # = 赋值是赋值内存地址，所以 x 也指向同样的内存地址，也就是说 x 跟 p1 指向同一个对象内存空间
print(p1.name)
print(x.name)


# 类属性可以通过类对象和实例对象获取
print(Person.type)  # 可以通过类对象获取类属性
print(p1.type)  # 可以通过实例对象来获取类属性,哪怕没有保存在对象空间


# 类属性只能通过类对象来修改，实例对象无法修改类属性
p1.type = 'human'  # 并不会修改类属性，反而给实例对象新增了一个属性

Person.type = 'Monkey'  # 只能通过类属性修改
print(Person.type)
print(p2.type)
print(p1.type)  # human 会优先调用自己的对象属性，即之前新增的属性
