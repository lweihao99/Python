# 使用 pd.read_csv 来读取csv文件
import pandas as pd

# pandas 读取csv中的文件的方法,甚至可以读取剪贴板
df = pd.read_csv('./Python 数据分析/Pandas/dogNames2.csv')
print(df)  # dataframe 类型,一个二维数据

# 读取MYsql数据库 ==> pd.read_sql(sql_sentence.connection) 就是sql的语句和链接就可以

# 读取mongodb,需要先链接mongo,读取数据库的数据,赋值给一个变量,然后传给pandas就可以了
