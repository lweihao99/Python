# datetime 模块
# 主要涉及 date类 用来显示日期，time类 用来显示时间，dateteime类 用来显示日期时间类，timedelta类 用来计算时间

import datetime as dt

# 以一个下划线 _ 开始
# 以两个下划线 __ 开始
# 以两个下划线开始 再以两个下划线结束 __x__ 每个都有特殊的含义

dt.datetime.now()  # 拿到当前的时间， datetime 类
dt.date(2020, 1, 1)  # 创建一个日期, date 类
dt.time(18, 23, 45)  # 创建一个时间， time类
dt.datetime.now() + dt.timedelta(3)  # 计算三天以后的日期时间， timedelta类

# 注意:内置类有:
# list tuple int str
