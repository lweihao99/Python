import matplotlib.pyplot as plt
import numpy as np

# 绘制10种大小和100种颜色的散点图

np.random.seed(0)  # 执行多次方法，但每次获取随机数是一样的
# 随机生成x
x = np.random.rand(100)  # 在 0.0-1.0之间随机生成100个数字
# 使用同样的方法生成y坐标
y = np.random.rand(100)

# 生成10种大小
# size = np.random.rand(10)*1000  # 由于数字比较小(0-1之间)所以*1000
size = np.random.rand(100)*1000  # 当大小size的个数小于点的个数时报错,所以点的个数和大小的个数必须一致
# 生成100种颜色
color = np.random.rand(100)  # 点的个数和颜色的个数要相同
# 绘制散点图
plt.scatter(x, y, s=size, c=color, alpha=0.7)  # s:大小, c:颜色,alpha:表示透明度
plt.show()
