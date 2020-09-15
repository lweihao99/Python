# 希望了解英国的YouTube中视频的评论和喜欢数的关系,应该如何绘制改图
from matplotlib import pyplot as plt
import numpy as np

# us_file_path = "./Python 数据分析/youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./Python 数据分析/youtube_video_data/GB_video_data_numbers.csv"

# data_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")
data_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 去除那些没有什么用的数据,只取喜欢书小于50k的,需要保持两个数据的一致性comment and likes
data_uk = data_uk[data_uk[:, 1] <= 500000]  # 这样之后所有的数据都是比50k要小的数据

data_uk_comment = data_uk[:, -1]
data_uk_likes = data_uk[:, 1]

plt.figure(figsize=(16, 8), dpi=100)
plt.scatter(data_uk_likes, data_uk_comment)

plt.show()
