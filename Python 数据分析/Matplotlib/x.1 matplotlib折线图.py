from matplotlib import pyplot as plt
import random

# 设置图片大小 figure 方法
fig = plt.figure(figsize=(20, 8), dpi=80)
"""
figure:图形图标的意思，在这里指的就是就是我们画的画,
通过实例化一个figure并且传递参数，能够在后台自动使用该figure实例
在图像模糊的时候可以传入dpi，让图片更加的清晰, dpi = dot per inch 每英寸的点，比如dpi = 80 就是每英寸有80像素点
"""

# 一天每隔2小时(x)的气温(y)
x = range(2, 26, 2)  # 步长2
y = [15, 13, 14.5, 17, 20, 25, 26, 27, 24, 22, 18, 15]

# 绘制
plt.plot(x, y)

# 手动指定x轴的刻度
_xticks_labels = [i/2 for i in range(4, 49)]
plt.xticks(_xticks_labels[::3])  # 要是想要一个更加密集的x轴的画可以自定义一个,要是太密集的话可以使用列表的步长来解决
plt.yticks(range(min(y), max(y)+1))  # 设置y轴刻度

# 保存图片
# plt.savefig('Python 数据分析/Matplotlib/demo1.jpg')
# 显示图形
plt.show()
