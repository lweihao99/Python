"""
对于刚刚加载出来的数据,我如果只想选择其中的某一列(行),应该如何做呢?
其实操作很简单,和Python中列表的操作一样
"""
import numpy as np
GB_file_path = "./Python 数据分析/youtube_video_data/GB_video_data_numbers.csv"
US_file_path = "./Python 数据分析/youtube_video_data/US_video_data_numbers.csv"

# t1 = np.loadtxt(GB_file_path, delimiter=",", dtype="int")  # 如果不加其他参数会报错
t2 = np.loadtxt(GB_file_path, delimiter=",", dtype="int")  # 如果不加其他参数会报错

print(t2)

print("*"*100)

# 取行
print(t2[2])

# 去连续的多行
print(t2[2:])

# 去不连续的多行
print(t2[[2, 8, 10]])  # 取不连续的多行不能直接输入多个数字,需要一个列表

# print(t2[1, :])  # 通用方法,取行也能使用,这里 冒号 之后什么都没写,表示每一列都要,在冒号之前的数字代表行数,之后的代表列数
# print(t2[2:, :])
# print(t2[[2, 4, 6], :])

# 取列
print(t2[:, 0])

# 去连续的多列
print(t2[:, 2:])  # 取三列之后的每一列

# 去不连续的多列
print(t2[:, [0, 2]])  # 取第0列和第3列

# 取多行和多列,比如取第三行,第四列的值
print(t2[2, 3])  # 类型是numpy.int64 # 就是numpy里的数值类型

# 取多行多列,第三行倒第五行,然后第二列倒第四列的结果
# 取得是行和列的交叉点的位置
b = t2[2:5, 1:4]
print(b)

# 取多个不相邻的点
# 选出来的结果是(0,0),(2,1),(2,3)
# 就是numpy的切片
c = t2[[0, 2, 2], [0, 1, 3]]  # 就是取 0,0的值,2,1的值,2,3的值
print(c)
