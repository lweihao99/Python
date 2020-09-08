"""
假设大家在30岁的时候，根据自己的实际情况，同级出来了从11岁到30岁每年交的男/女朋友的数量如列表a，请绘制出该数据的折线图，以便分析自己每年交女/男朋友的数量走势
"""
import matplotlib.pyplot as plt

my_fig = plt.figure(figsize=(18, 8), dpi=100)

# 设置x,y轴
x = range(11, 31)
a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]

plt.plot(x, a)

# 设置字体
plt.rcParams['font.sans-serif'] = ["SimHei"]

# 设置刻度
x_ticks = ['{}岁'.format(i) for i in x]
y_ticks = [i/2 for i in range(0, 19)]
plt.xticks(x, x_ticks)
plt.yticks(y_ticks)

# 添加描述信息
plt.xlabel('年龄从11岁到30岁')
plt.ylabel('每年交往次数', rotation=90)
plt.title("每年交往过的女/男朋友数量走势")

# 设置网格,为了能更好的看数据,可以使用轴刻度来定义网格
plt.grid(alpha=0.3)  # alpha:网格线条透明度

plt.show()
