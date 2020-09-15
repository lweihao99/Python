# 英国和美国各自YouTube1000的数据结合之前的matplotlib绘制出各自的评论数量的直方图
# 希望了解英国的YouTube中视频的评论和喜欢数的关系,应该如何绘制改图
from matplotlib import pyplot as plt
import numpy as np

us_file_path = "./Python 数据分析/youtube_video_data/US_video_data_numbers.csv"
# uk_file_path = "./Python 数据分析/youtube_video_data/GB_video_data_numbers.csv"

data_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")
# data_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 观看人数 , 喜欢 , 不喜欢 , 评论数量
# 取第四列数组,取到评论的数据
data_us_comments = data_us[:, -1]

# 选择比5000小的数据,因为大于5000的数据太少了,没有必要去统计
data_us_comments = data_us_comments[data_us_comments <= 5000]

print(data_us_comments.max(), data_us_comments.min())

d = 100
bin_nums = (data_us_comments.max() - data_us_comments.min()) // d

# 绘制图
plt.figure(figsize=(16, 8), dpi=100)

plt.hist(data_us_comments, bin_nums)

plt.grid()
plt.show()
