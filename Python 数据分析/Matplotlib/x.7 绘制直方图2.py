"""
在美国2004人口普查发现有 124million 的人在相对较远的地方工作.根据他们从家倒上班地点所需时间,通过抽样统计(最后一列)出了一下数据,这些数据能够绘制成直方图么?
"""
# 绘制条形图来模拟直方图的效果
from matplotlib import pyplot as plt

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]  # 组距不同
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

fig = plt.figure(figsize=(16, 8), dpi=100)

# 绘制
plt.bar(range(len(quantity)), quantity, width=1)  # 默认宽度是0.8
# 设置x轴的刻度
_x = [i-0.5 for i in range(13)]
_xtick_label = interval+[150]
plt.xticks(_x, _xtick_label)

plt.grid(alpha=0.4)

plt.show()

# 如果想要使用一些其他的matplotlib图形样式可以取matplotlib官网 http://matplotlib.org/gallery/index.html

# 其他的画图工具有 Echarts,plotly
