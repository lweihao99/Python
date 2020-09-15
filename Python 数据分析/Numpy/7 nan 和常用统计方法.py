# 什么时候会出现nan:当我们读取本地的文件为float的时候,如果有缺失,就会出现nan,当做了一个不合适的计算的时候(比如无穷大(inf)-无穷大)
# 注意:infinity,inf 表示正无穷,-inf表示负无穷,比如一个数字除以0在Python里会报错,但是在numpy中是一个inf或者-inf
import numpy as np
GB_file_path = "./Python 数据分析/youtube_video_data/GB_video_data_numbers.csv"

t2 = np.loadtxt(GB_file_path, delimiter=",", dtype="int")  # 如果不加其他参数会报错


# numpy中的nan的注意点
# 1.两个nan是不相等的
np.nan == np.nan  # ==> False

# 2. np.nan != np.nan

# 可以利用以上特性,判断数组中nan的个数
t2[:, 0] = 0
np.count_nonzero(t2)  # 会指出所有不为0的数值

np.count_nonzero(t2 != t2)  # 只有在nan的位置,t != t,所以可以指出nan的个数

# 通过no.isnan(t)来判断,一个数字是否是nan,返回bool类型,比如可以通过这个方式,将nan替换成0
np.isnan(t2)  # 跟 t!=t,的结果是一样的
t2[np.isnan(t2)] = 0

# 3. nan和任何值计算的结果都是nan,所以加求和的时候需要替换nan成数值,但是直接替换的时候会有影响,所以通常会替换成均值
# np.sum()是求和的方法,要是没有指定轴的话,会直接算整个数组
a = np.sum(t2)

t3 = np.arnage(12).reshape((3, 4))

# axis代表轴,就是计算哪个方向的和,比如要是axis=0那就么算出的结果是和行数一样的,就是算行上的结果,axis=1就是算列上的结果,得到的结果跟列数一样
np.sum(t3, axis=0)

# 替换成均值,要是替换成0要是平均值>0,那么之后的数值就会变小,所以一般会把缺失的数值替换为均值(中值)或者是直接删除有缺失值的一行
# 要是想要删除有缺失值的一行(列)需要在pandas中介绍

# 一些numpy中常用的统计函数
"""
1.t2.sum(axis=None):求和
2.t2.mean(a,axis=None):算均值
3.np.median(t2,axis=None):中值
4.t2.max(axis=None):最大值
5.t2.min(axis=None):最小值
6.np.ptp(t2,axis=None):极值,也就是最大值和最小值的差
7.t2.std(axis=None):标准差(SQM,scarto quadratico medio),这是一组数据平均值分散程度的一种度量.一个较大的标准差,代表大部分数值和其平均值之间差异较大;
一个较小的标准差,代表这些数值较接近平均值反映出数据的波动稳定情况,越大表示波动越大,越不稳定.
"""
