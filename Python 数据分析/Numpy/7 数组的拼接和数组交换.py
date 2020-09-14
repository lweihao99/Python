import numpy as np

us_file_path = "./Python 数据分析/youtube_video_data/GB_video_data_numbers.csv"
uk_file_path = "./Python 数据分析/youtube_video_data/US_video_data_numbers.csv"

t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int")
t2 = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

print(t1)
print("*"*100)
print(t2)
print("*"*100)

# 拼接两个数组的方法是 np.vstack((t1,t2))-->竖直拼接(vertically)竖着画条线,与之相反竖直分隔是横着画条线
print(np.vstack((t1, t2)))

print("*"*100)
# 另一个拼接方法 np.hstack((t1,t2)-->水平拼接(horizontally)横着画条线,与之相反而水平分隔是竖着画条线
print(np.hstack((t1, t2)))

# 在数组进行水平拼接或者竖直拼接的时候需要注意的是:
# 在竖直拼接的时候注意,每一列代表的意义相同,如果每一列的意义不同,这个时候应该交换某一组的数的列,让其和另外一类相同
# 水平拼接同理

# 数组的行列交换
t = np.arange(12, 24).reshape(3, 4)
# 如果想要把第一行和第二行进行交换
t[[1, 2], :] = t[[2, 1], :]  # 进行行交换
# 如果想要进行第一列和第二列进行交换
t[:, [0, 2]] = t[:, [2, 0]]  # 进行列交换
