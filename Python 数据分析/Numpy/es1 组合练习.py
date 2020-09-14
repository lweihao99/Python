# 英国和美国各自YouTube1000的数据结合之前的matplotlib绘制出各自的评论数量的直方图
# 希望了解英国的YouTube中视频的评论和喜欢数的关系,应该如何绘制改图
from matplotlib import pyplot as plt
import numpy as np

us_file_path = "./Python 数据分析/youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./Python 数据分析/youtube_video_data/GB_video_data_numbers.csv"

data_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")
data_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 观看人数 , 喜欢 , 不喜欢 , 评论数量
# 取第四列数组
t1 = data_uk[0:1000, 3]

# 组距
bin_width = 6000
# 极差
a = max(t1) - min(t1)
# 组数
num_bins = a//bin_width

plt.figure(figsize=(16, 8), dpi=100)

# 绘制
plt.hist(t1, num_bins)

# 设置刻度
plt.xticks(range(min(t1), max(t1)+bin_width, bin_width), rotation=45)
plt.yticks()
plt.grid()
plt.show()
