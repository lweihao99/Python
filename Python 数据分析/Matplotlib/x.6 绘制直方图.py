"""
假设你获取了250部电影的时长(列表a中),希望统计出这些电影时长的分布状态(比如时长为100分钟倒120分钟电影的数量,出现的频率)等信息,你应该如何呈现这些数据?
"""
from matplotlib import pyplot as plt
import random

a = []

count = 0
while count < 250:
    x = random.randint(86, 140)
    a.append(x)
    count += 1

fig = plt.figure(figsize=(16, 8), dpi=100)
# 设置字体
# plt.rcParams['font.sans-serif'] = ['Aria Unicode MS']
# 计算组数
bin_width = 3  # 组距
num_bins = (max(a)-min(a))//bin_width  # 组数,如果不能被整除,图会有偏差
# 如何算出适合的组数? 公式是:组数=极差/组距=max(a)-min(a)/bin width,组数是为了能更好的观察数据,如果组数太少会有统计误差,太多规律不明显
# 组距就是每一组的间隔
# 如果数据太分散组距就要很大,不然会有太多的组数

# 绘制直方图
# 直方图需要将数据分组
# 没有normed这个属性,换成了density,这个是频率分布直方图,没有density参数的是平数分布直方图
# 频率分布直方图就是算单个数据占总数据的多少比率,frequenza relativa
plt.hist(a, num_bins, density=True)

# 设置刻度
# max(a)+bin_width 保证取倒最大值
plt.xticks(range(min(a), max(a)+bin_width, bin_width))

plt.grid()


plt.show()

# 那些已经统计好的数据,统计之后的数据,是不能使用直方图绘制的,这种需要绘制条形图,通过条形图的方法来达到直方图的效果
# 只有没有经过统计过的数据可以使用直方图绘制也就是使用hits这个方法

# 直方图的一些应用场景
# 1.用户的年龄分布状态
# 2.一段时间内用户点击次数的分布状态
# 3.用户活跃时间的分布状态
