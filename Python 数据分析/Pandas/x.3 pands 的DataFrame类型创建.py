# 创建DataFrame,一个二维的数据
import pandas as pd
import numpy as np
t = pd.DataFrame(np.arange(12).reshape(3, 4))
print(t)  # 分为行index和列columns
# 所以DataFrame对象既有行索引,又有列索引
# 行索引,表明不同行,横向索引,叫index,0轴,axis=0
# 列索引,表明不同列,纵向索引,叫columns,1轴,axis=1
t = pd.DataFrame(np.arange(12).reshape(
    3, 4), index=list('abc'), columns=list('WXYZ'))
print(t)

# DataFrame传入字典作为数据
d1 = {'name': ['xiaoming', 'lisi'], 'age': [20, 22], 'tel': [10086, 10010]}

t2 = pd.DataFrame(d1)
print(t2)  # key 是列名,value是数值

d2 = [{'name': 'xiaohong', 'age': 32, "tel": 10010}, {
    'name': "zhangsan", 'tel': 10000}, {'name': 'lisi', "age": 22}]
t3 = pd.DataFrame(d2)
print(t3)  # key作为列索引,有三条数据所以有三行,如果key对应的数值是缺失的会使用nan填充
