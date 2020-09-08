import pandas as pd
import numpy as np

"""pandas 简介
1.Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的.
2.Pandas 是python的一个数据分析包，最初由AQR Capital Management于2008年4月开发，并于2009年底开源出来.
3.数据结构:
    a.Series：一维数组，与Numpy中的一维array类似。二者与Python基本的数据结构List也很相近，其区别是：List中的元素可以是不同的数据类型，
    而Array和Series中则只允许存储相同的数据类型，这样可以更有效的使用内存，提高运算效率

    b.Time- Series：以时间为索引的Series.

    c.DataFrame：二维的表格型数据结构。很多功能与R中的data.frame类似。可以将DataFrame理解为Series的容器.

    d.Panel ：三维的数组，可以理解为DataFrame的容器.

Pandas 有两种自己独有的基本数据结构。读者应该注意的是，它固然有着两种数据结构，因为它依然是 Python 的一个库，所以，Python 中有的数据类型在这里依然适用，
也同样还可以使用类自己定义数据类型。只不过，Pandas 里面又定义了两种数据类型：Series 和 DataFrame，它们让数据操作更简单了
"""


# 创建序列
# 1. Series就如同列表一样，一系列数据，每个数据对应一个索引值
# Series 就是“竖起来”的 list
s = pd.Series([1, 3, 6, np.nan, 44, 1])  # 像列表，有他自己的index, Nan = None
print(s)  # 自动加上序号, dtype: 数列数字,是什么类型的数字
print('')
"""
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0

第一列生成的是index也就是索引值可以使用 s.index 来查看对象的索引,需要注意的是索引可以自定义
使用 s.values 查看对象的数据值
"""
# 自定义索引
s1 = pd.Series(['jack', 'man', 18], index=['name', 'gender', 'age'])
print(s1)
print('')
"""
name      jack
gender     man
age         18
dtype: object"""

# 当每个元素都有了索引值之后，就可以根据索引操作元素了，跟list里的操作一样类似于dict
# 根据索引查看其值和修改其值
print(s1['name'])  # jack
s1['name'] = 'lisa'
print(s1['name'])
print('')

# 另一种定义Series对象的方式，就是使用字典dict
s2 = pd.Series({'Python': 9000, 'c++': 9001, 'c#': 9002})
# s3 = pd.Series(s2)
print(s2)
print('')

# 如果自定义了索引，自定的索引会自动寻找原来的索引，如果一样的，就取原来索引对应的值,这个可以简称为"自动对齐"
s4 = pd.Series(s2, index=['java', 'c++', 'c#'])
print(s4)
"""
java       NaN # 在 Pandas 中，如果没有值，都对齐赋给 NaN
c++     9001.0 # 拿到了原来索引对应的值
c#      9002.0
dtype: float64
"""
print('')

# Pandas 有专门的方法来判断值是否为空
print(pd.isnull(s4))

# Series 也可以用isnull
print(s4.isnull())
print('')

# 对索引的名字，是可以从新定义的
s4.index = ['语文', 'math', 'english']
print(s4)
print('')

# Series的运算
# 对于 Series 数据，也可以做类似下面的运算
print(s4*2)
print(s4[s4 > 9000])
