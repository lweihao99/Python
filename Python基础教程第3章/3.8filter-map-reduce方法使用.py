# filter 是过滤,Python3 是内置类。Python2 的时候是内置函数
# 对可迭代对象进行过滤，得到的是一个filter对象

ages = [12,14,21,22,16,22,19]
# filter 可以给定两个参数，第一个参数是函数，第二个参数是可迭代对象
# filter 结果是一个 filter 类型的对象, filter 对象也是一个可迭代对象
x = filter(lambda ele:ele>18,ages) # 选出>18的
# print(x) # <filter object at 0x0000028F99BFC370>
# for a in x:
#     print(a)

adult = list(x) # 转化成列表
print(adult)



# map就是将每一个元素都执行一遍函数
ages = [12,14,21,22,16,22,19]
m = map(lambda ele:ele+2,ages) # 将每个数字都+2
print(list(m))


# reduce 以前是一个内置函数
# 内置函数和内置类都在 builtin.py 文件里
from functools import reduce

def foo(x,y): # x=100, y=90--> x=190 (就是上两个数的和), y=89 --> x=279(之前两数的和),y=91--> ...x=370, y=80---> x=450
    return x + y


score = [100,90,89,91,80]
# print(reduce(lambda ele1,ele2:ele1+ele2,score)) # 求和
print(reduce(foo,score)) # 求和



# 求 age 的和
students = [
    {'name':'alex','age':19,'score':98,'height':180},
    {'name':'jack','age':21,'score':90,'height':187},
    {'name':'lisa',"age":22,'score':100,'height':168},
    {'name':'tony','age':20,'score':100,'height':189},
    {'name':'henry','age':23,'score':95,'height':178},
]

# def bar(x,y):
#     return x+y['age']

# 后面的0是初始化的值
# 初始化之后 x = 0, 
# y = {'name':'alex','age':19,'score':98,'height':180}
# a = reduce(bar,students,0)
a = reduce(lambda x,y:x+y['age'],students,0) # 也可以使用lambda表达式
print(a)
