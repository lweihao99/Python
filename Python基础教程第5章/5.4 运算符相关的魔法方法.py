class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, value):  # 这里的value 是 p2, 由于是 p1.__eq__(p2), 也就是p1调用的方法,所以sel就是p1
        # if self.name == value.name and self.age == value.age:  # 这里就是比较 p1==p2
        #     return True
        # # return ('__eq__方法被调用了,value=', value)
        # return False
        # 更加简洁的写法
        return self.name == value.name and self.age == value.age  # 优化了写法,一样就返回True否则False

        # 1. 调用__new__ 方法申请内存空间, 所以每生成一个对象就会申请一个新的内存空间
p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)
p3 = Person('zhangsan', 19)

# p1 和 p2 是同一个对象吗? 不是
# 如何比较两个对象是否是同一个对象? 比较的是内存地址
print('0x%X' % id(p1))  # 0x1FFBD634C10
print('0x%X' % id(p2))  # 0x1FFBD6AC340

# is 身份运算符 可以用来判断两个对象是否是同一个对象
print(p1 is p2)  # False
# 这里__eq__ 如果不重写，默认比较依然是内存地址
print(p1 == p3)  # False, 本质是调用 p1.__eq__(p2), 就是获取__eq__的返回值


nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
# is 比较两个对象的内存地址
print(nums1 is nums2)  # False, 这两个也是不同的内存空间
# == 会调用对象的 __eq__ 方法，然后获取这个方法的比较结果
# 在列表里是会自动写重写__eq__比较列表里的单独元素是否一样
print(nums1 == nums2)  # True,
