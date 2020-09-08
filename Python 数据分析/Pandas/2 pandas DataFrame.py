import pandas as pd
import numpy as np

"""
DataFrame 是一种二维的数据结构，非常接近于电子表格或者类似 mysql 数据库的形式。它的竖行称之为 columns，
横行跟前面的 Series 一样，称之为 index，也就是说可以通过 columns 和 index 来确定一个主句的位置"""

data = {"name": ['google', 'baidu', 'yahoo'],
        "marks": [100, 200, 300], "price": [1, 2, 3]}
dates = pd.date_range('20200903', periods=6)
print(dates)
print('')
"""
DatetimeIndex(['2020-09-03', '2020-09-04', '2020-09-05', '2020-09-06',
               '2020-09-07', '2020-09-08'],
              dtype='datetime64[ns]', freq='D')"""


# 生成DataFrame
df = pd.DataFrame(np.random.randn(6, 4), index=dates,
                  columns=['a', 'b', 'c', 'd'])
"""
np.random.randn(行数,列数)生成随机数,这是numpy生成的,
index=dates 按照index的名字来排序，这里由于用的是dates，所以使用的是排序好的日期,跟 Series 类似的，DataFrame 数据的索引也能够自定义
columns=生成列名,在 DataFrame 中，columns 跟字典键相比，有一个明显不同，就是其顺序可以被规定,就像上面那样"""
print(df)
print('')


# 不给行数名和列名，使用pandas默认生成
df1 = pd.DataFrame(data)
print(df1)
print('')
"""默认生成的
      name  marks  price
0  google    100      1
1   baidu    200      2
2   yahoo    300      3"""

"""
定义一个 DataFrame 对象的常用方法——使用 dict 定义,字典里的key对应DataFrame的colums值也就是列名,字典里每个value是一个列表，它们就是那一竖列中的具体填充数据
由于没有确定索引，所以默认从0开始排列，从上面的结果中很明显表示出来，这就是一个二维的数据结构（类似 excel 或者 mysql 中的查看效果）"""


# 可以使用字典来排序
df2 = pd.DataFrame({
    'A': 1,
    'B': pd.Timestamp('20200101'),  # 全部输出20200101
    # 要输出的数据是1,生成的列表范围是4,数据类型float32
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3]*4, dtype='int32'),  # 输出3行数4，数据类型int32
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'foo'
})

print(df2)
print('')

"""使用字典的df2输出结果
   A          B    C  D      E    F
0  1 2020-01-01  1.0  3   test  foo
1  1 2020-01-01  1.0  3  train  foo
2  1 2020-01-01  1.0  3   test  foo
3  1 2020-01-01  1.0  3  train  foo"""

print(df2.dtypes)  # 会返回dtype


# 定义 DataFrame 的方法，除了上面的之外，还可以使用“字典套字典”的方式
new_data = {'lang': {'first': 'python', 'second': 'java'},
            'price': {'first': 2000, 'third': 3000}}

df3 = pd.DataFrame(new_data)
print(df3)
"""
         lang   price
first   python  2000.0
second    java     NaN
third      NaN  3000.0"""

# 在字典中就规定好数列名称（第一层key）和每横行索引（第二层字典key）以及对应的数据（第二层字典value），也就是在字典中规定好了每个数据格子中的数据，没有规定的都是空


# DataFrame可以通过索引colums来获取，对应竖列的所有内容,以及其对应的index
print(df1['name'])

# 可以通过索引colums来给一列赋值
df2['F'] = 'man'
print(df2)
"""
   A          B    C  D      E    F
0  1 2020-01-01  1.0  3   test  man
1  1 2020-01-01  1.0  3  train  man
2  1 2020-01-01  1.0  3   test  man
3  1 2020-01-01  1.0  3  train  man"""


"""也可以单独的赋值，除了能够统一赋值之外，还能够“点对点”添加数值，
结合前面的 Series，既然 DataFrame 对象的每竖列都是一个 Series 对象，那么可以先定义一个 Series 对象，然后把它放到 DataFrame 对象中"""

new_demo = pd.Series(['hello', 'bye', 'yoo'], index=[0, 1, 2])
df2['F'] = new_demo
print(df2)
"""
   A          B    C  D      E      F
0  1 2020-01-01  1.0  3   test  hello
1  1 2020-01-01  1.0  3  train    bye
2  1 2020-01-01  1.0  3   test    yoo
3  1 2020-01-01  1.0  3  train    NaN"""

# 还可以更精准的修改数据吗？当然可以，完全仿照字典的操作
df3['price']['second'] = 'helloo'  # 第一个指定列名colums，第二个指定行数名也就是index
print(df3)
"""
          lang   price
first   python    2000
second    java  helloo
third      NaN    3000"""

# 一些DataFrame 简单的指令
# 1.获取行索引
print(df1.index)

# 2.获取列索引
print(df1.columns)

# 3.获取行以及列索引
print(df1.axes)

# 4.index 与 colums对调
print(df1.T)

# 5.打印DataFrame对象的信息
print(df1.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    3 non-null      object
 1   marks   3 non-null      int64 
 2   price   3 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 200.0+ bytes
None"""

# 6.head(i)获取前i行数据
print(df1.head(2))

# 7.tail(i)现实后i行数据,包括i本身
print(df1.tail(2))

# 8.describe() 查看数据按列的统计信息,可显示数据的数量、缺失值、最小最大数、平均值、分位数等信息
print(df1.describe())
"""
       marks  price
count    3.0    3.0
mean   200.0    2.0
std    100.0    1.0
min    100.0    1.0
25%    150.0    1.5
50%    200.0    2.0
75%    250.0    2.5
max    300.0    3.0"""
