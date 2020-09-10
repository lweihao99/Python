# numpy 的优点是:快速,方便,科学计算基础库
# 是一个重在数值计算的科学计算的基础库,多用于在大型,多维数组上执行数值运算
# 数组就是一个列表,或者多个列表嵌套列表
import numpy as np
import random
# 使用numpy创建数组,得到ndarray的类型
t1 = np.array([1, 2, 3])  # numpy 数组类型:<class 'numpy.ndarray'>

t2 = np.array(range(10))

t3 = np.arange(10)  # 快速生成一个数组
print(t3)  # [0 1 2 3 4 5 6 7 8 9] , arrange 跟 array(range()) 差不多,是numpy独有的方法

print(t3.dtype)  # dtype 是数组的里数据的类型,有很多其他的数据类型比如:float64,float32...etc
# 对于数据的使用是根据内存的大小决定的,当数据很少的时候没关系,但是,要是数据很多的时候就要指定数据类型,来保证数据大小
# 指定数据类型
t4 = np.array(range(1, 4), dtype=float)
print(t4.dtype)  # float64

# numpy中的bool类型
t5 = np.array([1, 1, 0, 1, 0, 0], dtype=bool)
print(t5)  # [ True  True False  True False False] 转换成bool类型

# 调整数据类型
t6 = t5.astype('int8')
print(t6)  # [1 1 0 1 0 0]
print(t6.dtype)  # int8

# numpy 中的小数
# 随机生成10个小数,这里想要取固定小数需要 "%.nf"%random.random(),n是想要取的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)

t8 = np.round(t7, 2)  # 取小数,这里就是取2个小数,使用这个方法可以保留固定位的小数
