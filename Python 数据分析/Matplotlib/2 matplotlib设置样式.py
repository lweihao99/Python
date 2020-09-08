# 设置标签文字和线条粗细

# 示例:绘制折线图并设置样式
import matplotlib.pyplot as plt

# 设置点
dev_x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
dev_y = [120, 500, 600, 650, 780, 900, 660, 1220, 1600, 5000]

# 调用绘图方法，并设置线条样式
plt.plot(dev_x, dev_y, linewidth=5)  # linewidth设置线条宽度

# 设置图标标题，并在坐标轴上添加标签
# 这个方式可以显示中文,就是设置一个支持中文的字体,当然还有很多其他的方式
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('折线图', fontsize=24)  # 设置图标名称,直接使用中文来设置图标名称会乱码,因为matplotlib默认不支持中文
# 设置x轴名称
plt.xlabel('data', fontsize=24)
# 设置y轴名称
plt.ylabel('squares', fontsize=24)

plt.show()
