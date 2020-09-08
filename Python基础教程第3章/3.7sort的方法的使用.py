# 列表有几个内置函数和内置类，用到了匿名函数
nums = [4, 8, 2, 1, 3]
nums.sort()  # 将列表排序成有序，会直接对列表进行排序
print(nums)

# sorted 是内置函数，不会改变原有的数据，而是生成一个新的结果
# sorted(nums) # 这个是无序的
x = sorted(nums)  # 将新生成的一个新的结果赋值给变量 x， 是有序的
print(x)

ints = (3, 2, 7, 4, 9, 5, 2, 63, 1)
a = sorted(ints)
print(a)  # 可以生成一个新的排序好的元组

students = [
    {'name': 'alex', 'age': 19, 'score': 98, 'height': 180},
    {'name': 'jack', 'age': 21, 'score': 90, 'height': 187},
    {'name': 'lisa', "age": 22, 'score': 100, 'height': 168},
    {'name': 'tony', 'age': 20, 'score': 100, 'height': 189},
    {'name': 'henry', 'age': 23, 'score': 95, 'height': 178},
]

# students.sort() # 会报错,因为比较不了,所以字典和字典之间不能使用(sort)比较运算
# 设定一个比较规则，传递参数key
# key 需要的是一个函数,参数类型是函数


def foo(ele):
    return ele  # 通过返回值告诉sort方法，按照元素的那个属性进行排序
    pass
# students.sort(key=foo) # 会报错，因为sort他自己调用了函数,并传了参数进去
# TypeError: foo() takes 0 positional arguments but 1 was given
# foo这个函数需要0个位置参数，但是在调用的时候传递了一个参数
# 所以要给函数添加一个参数
# students.sort(key=foo) # sort 自己传递的参数就是列表里的元素，遍历了至少一遍


# 可以用lambda来简化函数
students.sort(key=lambda ele: ele['score'], reverse=True)  # 直接在这里定义排序标准

print(students)
