import numpy as np
GB_file_path = "./Python 数据分析/youtube_video_data/GB_video_data_numbers.csv"
US_file_path = "./Python 数据分析/youtube_video_data/US_video_data_numbers.csv"

# t1 = np.loadtxt(GB_file_path, delimiter=",", dtype="int")  # 如果不加其他参数会报错
t2 = np.loadtxt(GB_file_path, delimiter=",", dtype="int")  # 如果不加其他参数会报错

# numpy 中的数值的修改,只需从新给数值进行赋值即可
t2[:, 2:4] = 0  # 从第三列倒第4列

print(t2 < 10)  # 返回bool类型
print(t2[t2 < 10]) = 3  # 将t2中小于10的数修改成3,也就是将True的值进行赋值,这叫布尔索引

# 使用numpy的三元运算 np.where()
np.where(t2 < 10, 0, 10)  # a = 0 if t2<10 else 10

# 将小于10的数字替换成0,把大于的20的替换成20
# 使用numpy中的clip(裁剪)
t2.clip(10, 20)  # 将小于10的替换成10,大于20的替换成20

# 强行赋值为Nan
t2[3, 3] = np.nan
# 会报错因为Nan是浮点型,但是t2的数值是整形的,随意需要将t2数组转化成整形在进行赋值
t2 = t2.astype(float)
t2[3, 3] = np.nan
