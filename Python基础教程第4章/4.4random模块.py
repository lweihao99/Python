# random 模块 用来生成一个随机数

import random

# randint(a,b) 用来生成 [a,b] 的随机整数 randint(a,b) == randrange(a,b+1)
random.randint(2, 9)
random.random()  # random() 用来生成 [0,1) 的随机的浮点数

random.randrange(2, 9)  # randrange(a,b) 用来生成 [a,b)的随机整数

# choice() 用来在可迭代对象里随机抽取一个数据
print(random.choice(['zhangsan', 'lisi', 'lisa', 'linda', 'jack', 'jerry']))

# sample 用来在可迭代对象里随机抽取 n 个数据
random.sample(['zhangsan', 'lisi', 'lisa', 'linda',
               'jack', 'jerry'], 2)  # 每次随机2个
