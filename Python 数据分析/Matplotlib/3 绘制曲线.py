# 绘制一元二次方程的曲线 y=x^2
# Matplotlib 有很多函数用于绘制各种图形，其中plot函数用于曲线，需要将200个点的x坐标和y坐标分别以序列的形式传入plot函数

import matplotlib.pyplot as plt
# 200个点的x坐标
x = range(-100, 100)
# 生成y坐标
# 生成200个 y = x**2,不强制转换成list，默认是generator而matplotlib不能使用generator作为input
y = list((i**2 for i in x))

# 绘制一元二次曲线
plt.plot(x, y)

# 调用savefig来保存图表
# plt.savefig('./result.jpg')  # 不写格式的话，默认是png

plt.show()
