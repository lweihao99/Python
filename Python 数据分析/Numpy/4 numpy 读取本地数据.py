# numpy 读取数据,通常来讲用的比较少,因为pandas的功能更加的强大
"""
numpy通常都是从csv文件里读取数据,也就是逗号分隔值文件(Comma-Separated Value)

numpy 的读取方法是 np.loadtxt(),这个方法是从文本文件里读取内容
loadtxt的参数有:
    frame:就是文件,字符串或产生器,也就是文件的路径
    dtype:数据类型,可选,csv的字符串以什么数据类型读入数组中,默认是 np.float
    delimiter:分隔字符串,就是以什么字符串来分隔数据
    skiprows:(row = 行),跳过前x行,一般跳过第一行表头
    usecols:读取指定的列,索引,是元祖类型
    unpack:如果True,读入属性将分别写入不同数组变量,False读入数据只写入一个数组变量,默认False,将行转成列,将列转成行
"""
# 假设这里有一个英国和美国各自YouTube 1000多个视频的点击,喜欢,不喜欢,评论数量(["views","likes","dislikes","comment_total"])的csv
import numpy as np
GB_file_path = "./Python 数据分析/youtube_video_data/GB_video_data_numbers.csv"
US_file_path = "./Python 数据分析/youtube_video_data/US_video_data_numbers.csv"

t1 = np.loadtxt(GB_file_path, delimiter=",", dtype="int")  # 如果不加其他参数会报错
t2 = np.loadtxt(GB_file_path, delimiter=",", dtype="int")  # 如果不加其他参数会报错

print(t1)
print(t2)

# 什么是转置?==> 转置就是一种变换,对于numpy中的数组来说就是在对角线方向交换数据,目的也是为了更方便的去处理数据

t3 = np.arange(24).reshape((4, 6))
# 转置的方法有
t3.transpose()

t3.T

t3.swapaxes(1, 0)  # 交换轴,就是行和列进行变换
