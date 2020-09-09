# 假设通过爬虫你获取到了北京2016年3,10月份每天白天的最高气温(分别位于列表a,b)那么此时如何寻找出气温和随时间(天)变化的某种规律?
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(
    fname="/System/Library/Fonts/PingFang.ttc")
fig = plt.figure(figsize=(15, 7), dpi=100)
a_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17,
       18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22, 23]
b_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17,
        20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12, 13, 6]
x_3 = range(1, 32)  # 31天
x_10 = range(51, 82)  # 31天,用来分开x_3和x_10

# 设置字体
# plt.rcParams['font.family'] = ['Songti']

# 绘制
plt.scatter(x_3, a_3, label='March')
plt.scatter(x_10, b_10, label='November')  # 31天,用来分开x_3和x_10, b_10)

# 调整x轴的刻度
_x = list(x_3)+list(x_10)
_xtick_labels = ['Mar {}'.format(i) for i in x_3]
_xtick_labels += ['Nov {}'.format(i-50) for i in x_10]
plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=my_font, rotation=45)

# 添加描述信息
plt.xlabel("Datetime")
plt.ylabel('Temperature')
plt.title('Title')

# 添加图例
plt.legend()

# 展示
plt.show()

# 跟画折线图方法差不多,就是要使用scatter方法
# 散点图可以观察数据的离散程度,和不同条件(维度)之间的内在联系
