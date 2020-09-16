# 那么回到之前我们读取的狗名字统计的数据上,我们尝试一下刚刚的方法
import pandas as pd

# 那些名字使用次数最多
df = pd.read_csv('./Python 数据分析/Pandas/dogNames2.csv')
# print(df.head())
# print(df.info())  # 通过这个方法可以看到有一列数据缺失了三行

# 要想统计出使用最多的名字,我们需要先进行排序,也就是按照次数来进行排序
# DataFrame 中排序的方法
df = df.sort_values(by='Count_AnimalName', ascending=False)
# print(df.tail(10))  # 排序的方式默认是升序的,可以通过ascending参数来转换
print(df.head(5))  # 在转换了排序方式之后,前5个名字就是使用最多的,但是使用head方法不是属于切片的,不能单独研究单个数据
