from matplotlib import pyplot as plt
import numpy as np
# 使用plt函数绘制任何曲线的第一步都是生成若干个坐标点(x,y)
# 这次去 0 到 10 之间 100 个等差数作为 x 的坐，然后将这100个坐标一起传入numpy的sin和cos函数，就会得到100个y坐标值
# 最后使用plot函数绘制正弦和余弦曲线

# 生成 x 坐标
x = np.linspace(0, 10, 100)  # 0-10 的100个等差数列
sin_y = np.sin(x)
cos_y = np.cos(x)

plt.plot(x, sin_y)  # 绘制正弦曲线,第一个图默认蓝色
plt.plot(x, cos_y)  # 绘制余弦曲线

plt.show()
