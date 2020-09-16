# 如果读取的数据有很多数据是我不想要的
import pandas as pd

# DataFrame 的基础属性,其他方法可以看: <./Python 数据分析/Pandas/2 pandas DataFrame.py>
"""
1-df.shape # 行数,列数
2-df.dtype # 行数据类型
3-df.ndim # 数据维度
4-df.index # 行索引
5-df.columns # 列索引
6-df.values # 对象值,二维ndarray数组
"""

# DataFrame 整体情况查询
"""
1-df.head(3) # 显示头部几行,默认5行
2-df.tail(3) # 显示末尾几行,默认5行
3-df.info() # 相关信息概览:行数,列数,列索引,列非空值个数,列类型,行类型,内存占用
4-df.describe() # 快速综合统计结果:计数,均值,标准差,最大值,四分位数,最小值,只有数字类型能被统计
"""
