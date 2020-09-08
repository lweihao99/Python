# 绘制子图
# 将画布分为区域，将图画到画布的指定区域
import matplotlib.pyplot as plt
import numpy as np

# 设置x坐标
x = np.linspace(1, 10, 100)

# 将画布分为2行2列，将图都画到画布的1区域
plt.subplot(2, 2, 1)
# 修改x,y轴的坐标大小,可看范围
plt.xlim(-5, 20)
plt.ylim(-2, 2)

# 绘图
plt.plot(x, np.sin(x))

# 将画布分为2行2列,并将图画到画布的3区域
plt.subplot(2, 2, 3)
# 修改y坐标可看范围
plt.ylim(-2, 2)
# 绘图
plt.plot(x, np.cos(x))

plt.show()  # 分不同的画布来展示正弦和余弦曲线
