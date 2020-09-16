# numpy 能够帮我们处理数值形的数据,但是字符串,还有时间序列等数据需要pandas来处理.
# 比如一些我们通过爬虫获取到的存储倒数据库中的数据
# 所以numpy能够办我们处理数值,但是pandas除了处理数值之外(基于numpy),还能够帮我们处理其他类型的数据.

# pandas里常用的数据类型有:1.Series一维数据,带标签数组,2.DataFrame二维数据,Series容器

import pandas as pd

print(pd.Series([1, 2, 3, 4, 5]))  # 第一列是索引,第二列是数据
# 标签就是索引
# 指定索引需传入index参数即可
print(pd.Series([1, 2, 3, 'hello', 'pandas'], index=['a', 'b', 'c', 'd', 'e']))

# 另一个方式来创建Series,也就是使用字典来创建
temp_dict = {'name': 'lisi', 'age': 22, 'tel': 199}
t1 = pd.Series(temp_dict)
print(t1)  # 使用字典来创建Series的话字典的key代表index,value代表数据
# 如果选中一些没有的数据会输出索引和nan
# print(t1.astype('float'))  # 操作跟numpy一样

# pandas 的切片和索引
print(t1['age'])

# 通过行数来索引
print(t1[1])

# 取连续或者不连续的多行
t1[:3]  # 取0行倒3行的数据

# 去不连续的
t1[[1, 2]]
t1[['age', 'tel']]  # 要是取一些不存在的index会得到nan

# bool索引
t = pd.Series([i for i in range(10)], index=[i for i in range(10)])
print(t[t > 4])  # 选中>4的数值,跟numpy中的操作一样

# Series的属性:index,value
# 取出index属性
print(t3.index)
print(i for i in t3.index)  # 是可迭代的长度
print(len(t3.index))  # 可以获取长度
list(t3.index)[:2]  # 由于是可迭代属性,可以转换成列表

# 取出value属性
print(t3.value)  # 是个np.ndarray 类型数据,是个numpy中的数组类型
# 可以进行迭代,切片,索引

# 所以Series就是以key,value组成的,分别是索引和数值

# ndarray 的很多方法都可以运用于Series类型,比如argmax,clip
# Series具有where方法,但是结果和ndarray不同
