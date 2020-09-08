"""
matplotlib 是Python的一个2D绘图库，可让数据可视化，更直观且真实的展示给用户,主要绘制散点图，直方图，柱状图
"""
# 引入matplotlib 软件包，导入 pyplot功能 并赋予名称 plt
from matplotlib import pyplot as plt

# 有两个使用matplotlib最常用的场景，画点和画线、

"""pyplot里的基本方法使用:
1.title():设置图标的名称
2.xlabel():设置x轴的名称
3.ylabel():设置y轴名称
4.xticks(x,ticks,rotation):设置x轴的刻度和rotation旋转角度
5.yticks(y,ticks,rotation):设置y轴的刻度和rotation旋转角度
6.plot():绘制线性图表
7.show():显示图表
8.legend():显示图例
9.text(x,y,text):显示每条数据的值，x,y值得位置
10.figure(name,figsize=(w,h),dpi=n):设置图片大小
"""
# 准备绘制的点
# X 轴
dev_x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Y 轴
dev_y = [120, 500, 600, 650, 780, 900, 660, 1220, 1600, 5000]

# 导入 X 轴 和 Y 轴
plt.subplot(2, 2, 1)
plt.plot(dev_x, dev_y)  # 折线

# 将 [0,1] 和 [2,4] 连起来
plt.subplot(2, 2, 2)
plt.plot([0, 2], [1, 4])  # 直线

# 一天每隔2小时(x)的气温(y)
x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

plt.subplot(2, 2, 3)
plt.plot(x, y)
# 显示图形
plt.show()
