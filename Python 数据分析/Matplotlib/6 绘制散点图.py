# 绘制散点图使用的函数是scatter,该函数需要接收x和y的序列
import matplotlib.pyplot as plt
import numpy as np

# 生成x坐标,100个等差数列
x = np.linspace(0, 10, 100)

# 使用scatter绘制散点图
plt.scatter(x, np.sin(x))

plt.show()
"""
如果点的形式没有差别，特指颜色，点的大小，连贯度,推荐使用plot，反之则必须使用scatter"""
