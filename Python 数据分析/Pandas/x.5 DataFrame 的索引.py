import pandas as pd
import numpy as np

# 那些名字使用次数最多
df = pd.read_csv('./Python 数据分析/Pandas/dogNames2.csv')
# print(df.head())
# print(df.info())  # 通过这个方法可以看到有一列数据缺失了三行

# 要想统计出使用最多的名字,我们需要先进行排序,也就是按照次数来进行排序
# DataFrame 中排序的方法
df = df.sort_values(by='Count_AnimalName', ascending=False)
# print(df.tail(10))  # 排序的方式默认是升序的,可以通过ascending参数来转换
print(df.head(5))  # 在转换了排序方式之后,前5个名字就是使用最多的,但是使用head方法不是属于切片的,不能单独研究单个数据

# 取前100行
print(df[:20])

# 只取单列
print(df[:20]['Row_Labels'])  # 取得具体某一列,数字的话就是行数
# pandas 取行或者列的注意点
# 1-[]写数组,表示取行,对行进行操作
# 2-[] 写字符串,表示取列索引,对列进行操作

# 同时取某些行和某些列的操作方法有两个:df.loc 通过标签(字符串)索引行数据, df.iloc 通过位置获取行数据

t3 = pd.DataFrame(np.arange(12).reshape((3, 4)),
                  index=list('abc'), columns=list('WXYZ'))

print(t3)

# 取某个单个数据
print(t3.loc['a', 'Z'])

# 取整行
print(t3.loc['a', :])

# 取整列
t3.loc[:, 'Y']

# 取多行
t3.loc[['a', 'c'], :]

# 取多列
t3.loc[:, ['W', 'Z']]

# 取多行多列
t3.loc[['a', 'c'], ['W']]


# 通过位置获取数据
# 取第三列
t3.iloc[:, 2]
# 取第二行
t3.iloc[1, :]

# 取多行多列
t3.iloc[1:, :2]

# 赋值
t3.iloc[1:, :2] = np.nan  # 在dataframe里会自动转换
