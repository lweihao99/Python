class Person(object):

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __setitem__(self, key, value):  # key = 'zhangsan'
        # 如果直接写 self.key 就是新加一个属性
        self.__dict__[key] = value  # 先转化成字典然后根据传入的key 和 value 根据传入的数据重新赋值

    def __getitem__(self, item):
        return self.__dict__[item]


p = Person('zhangsan', 18, 'Venezia')
print(p.__dict__)  # 将对象转化成为字典

# 不能直接把一个对象当做字典来使用,需要调用__setitem__方法
p['name'] = 'jack'  # [] 会调用对象的 __setitem__ 方法, []里的传入key参数，'jack'传入value参数
p['age'] = 20
print(p.name, p.age)


# 这个会直接自动调用 __getitem__
print(p['name'])  # 默认是不能直接调用字典的
