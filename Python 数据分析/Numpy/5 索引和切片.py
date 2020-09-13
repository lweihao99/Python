"""
对于刚刚加载出来的数据,我如果只想选择其中的某一列(行),应该如何做呢?
其实操作很简单,和Python中列表的操作一样
"""
import numpy as np
GB_file_path = "./Python 数据分析/youtube_video_data/GB_video_data_numbers.csv"
US_file_path = "./Python 数据分析/youtube_video_data/US_video_data_numbers.csv"

t1 = np.loadtxt(GB_file_path, delimiter=",", dtype="int")  # 如果不加其他参数会报错
t2 = np.loadtxt(GB_file_path, delimiter=",", dtype="int")  # 如果不加其他参数会报错

print(t1)
print(t2)
print("*"*100)
# 取行
print(t2[2])

# 去连续的多行
print(t2[2:])

# 去不连续的多行
print(t2)
