"""
假设你知道了列表a中电影分别在2017-09-14(b_14),2017-09-15(b_15),2017-09-16(b_16)三天的票房,为了展示列表中电影本身的票房
以及电影的数据对比情况,应该如何更加直观的呈现该数据?
"""
from matplotlib import pyplot as plt

a = ['猩球崛起3:终极之战', '敦刻尔克', '蜘蛛侠:英雄归来', '战狼2']
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

_y_14 = list(range(len(a)))  # 分开条形
_y_15 = [i+0.3 for i in _y_14]
_y_16 = [i+0.3*2 for i in _y_14]


plt.figure(figsize=(16, 8), dpi=100)
# 全局设置字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# 绘制
height = 0.2
plt.barh(_y_16, b_16, label='2017-09-16', height=height)
plt.barh(_y_15, b_15, label='2017-09-15', height=height)
plt.barh(_y_14, b_14, label='2017-09-14', height=height)

# 设置刻度
plt.yticks(_y_15, a)  # 电影名显示在中间

# 添加描述信息
plt.xlabel('日期时间')
plt.ylabel('电影')
plt.title('票房统计')

# 设置图例
plt.legend()

plt.show()
