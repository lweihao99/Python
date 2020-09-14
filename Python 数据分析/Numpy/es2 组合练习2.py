import numpy as np
# 现在希望把之前的es1 案例中两个国家的数据放到一起来研究分析,同事保留国家的信息(每条数据的国家来源),应该这么办?

us_data = "./Python 数据分析/youtube_video_data/US_video_data_numbers.csv"
uk_data = "./Python 数据分析/youtube_video_data/GB_video_data_numbers.csv"

# 加载国家数据
us_data = np.loadtxt(us_data, delimiter=",", dtype=int)
uk_data = np.loadtxt(uk_data, delimiter=",", dtype=int)

# 添加国家信息
# 在国家的数据最后或者一开始添加一列0或1来代表国家信息
# 构造全为0的数据
# zeros方法来生成0,需要基于形状,也就是行数和列数,这里us_data.shape[0]代表行数,1代表列
zeros_data = np.zeros((us_data.shape[0], 1)).astype(int)
ones_data = np.ones((uk_data.shape[0], 1)).astype(int)  # 生成1

# 分别添加一列全为0和1的数组
us_data = np.hstack((us_data, zeros_data))
uk_data = np.hstack((uk_data, ones_data))

# 拼接两组数据
final_data = np.vstack((uk_data, us_data))
print(final_data)
