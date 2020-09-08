from matplotlib import pyplot as plt
import random
import matplotlib as mpl
from matplotlib import font_manager
# 设置字体

# font = {'family': 'Fira Code',
#         'weight': 'bold',
#         'size': 'larger'}
# mpl.rc("font", **font)

# 另一种设置字体大小的方式

# my_font = font_manager.FontProperties(fname="/windows/fonts/simhei.ttf") # 然后在设置刻度里添加 fontproperties=my_font


# 设置图片大小
fig = plt.figure(figsize=(20, 9), dpi=100)
# 列表a表示10点到12点的每一分钟的气温，如何绘制折线图观察每分钟气温的变化情况?
x = range(0, 120)
a = [random.randint(20, 35) for i in range(120)]

plt.plot(x, a)

# 另一个设置字体的方法
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置可以显示中文的字体

# 设置刻度
_x = list(x)  # 太密集可以强制转换成列表，设置步长
_x_labels = ['10点{}分'.format(i)for i in range(0, 60)]
_x_labels += ['11点{}分'.format(i)for i in range(0, 60)]  # 刚好总和120个值

# 调整x轴的刻度
# 步长得到一一对应,数字得一致,这里前面设置了步长后面也得取相同的步长
plt.xticks(_x[::5], _x_labels[::5], rotation=45)  # rotation 是旋转的度数

# 添加描述信息
plt.xlabel('时间')
plt.ylabel("温度 单位℃", rotation=90)
plt.title("10点到12点，每分钟的气温变化情况")

plt.show()
