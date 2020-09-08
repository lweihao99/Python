"""
假设大家在30岁的时候，根据自己的实际情况，统计出来了你和你同桌各自从11岁到30岁每年交的女/男朋友的数量如列表a和b，请在一个图中绘制出该数据的折线图，以便比较自己和同桌20年间的差异，
同时分析每年交女/男朋友的数量走势
"""
import matplotlib.pyplot as plt

# 设置图片大小
fig = plt.figure(figsize=(18, 8), dpi=100)

x = range(11, 31)
a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
b = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 多次绘图，只需多次调用plot方法即可
# 设置 label 参数，在调用legend方法来展示图例,color参数设置颜色,linestyle定义线条样式
plt.plot(x, a, label="自己", color="#f08080",
         linestyle=":", linewidth=2)  # 颜色可以使用16进制rgb颜色值
plt.plot(x, b, alpha=0.6, label="同桌", color="cyan",
         linestyle="-.", linewidth=2)  # alpha:调节透明度
# 设置字体
plt.rcParams['font.sans-serif'] = ["SimHei"]

# 设置刻度
x_ticks = ['{}岁'.format(i) for i in x]
y_ticks = [i/2 for i in range(0, 15)]
plt.xticks(x, x_ticks)
plt.yticks(y_ticks)

# 添加描述信息
plt.xlabel('年龄从11岁到30岁')
plt.ylabel('每年交往次数', rotation=90)
plt.title("每年交往过的女/男朋友数量走势")

# 设置网格,为了能更好的看数据,可以使用轴刻度来定义网格
plt.grid(alpha=0.3)  # alpha:网格线条透明度

# 添加图例
plt.legend(loc="upper left")  # loc:location表示图例的位置，其他位置和功能的可以看方法源码

# 保存图片
plt.savefig("Python 数据分析/Matplotlib/折线图练习3.jpg")
# 展示
# plt.show()
