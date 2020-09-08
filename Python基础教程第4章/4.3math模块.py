# math 模块
# math 模块保存了数学计算相关的方法，可以很方便的实现数学运算
# 可以实现很多复杂运算

import math

# 常用的函数
math.factorial(6)  # 求阶乘

math.floor(12.98)  # 向下取整 12
math.ceil(15.001)  # 向上取整 16
math.pow(2, 10)  # 1024 幂运算 可以用 2**10 == pow(2,10) == math.pow(2,10)
round()  # 这是个内置函数，实现四舍五入到指定位数


# math.sin(30) # 要的是弧度(radiant) pi=180 所以要:
math.sin(math.pi/6)  # 无线接近 0.5
math.cos(math.pi/2)  # 无限接近于 0.5
