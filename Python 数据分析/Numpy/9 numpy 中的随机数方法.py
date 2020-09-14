import numpy as np

# 在numpy中生成随机数
# .rand(d0,d1,...dn)创建d0-dn纬度的均匀分布的随机数组,浮点数类型,范围(0,1)
np.random.rand(0, 2)

# .randn(d0,d1,d2,..dn)创建d0-dn纬度的标准正态分布随机数,浮点数,平均数0,标准差1
np.random.randn(0, 2)

# .randint(low,high,(shape))从给定上下限范围选取随机数整数,范围是 low high, 形状是shape
np.random.randint(0, 10, (4, 5))

# .uniform(low,high,(size))产生具有均匀分布的数组,low起始值,high结束值,size形状,不在是整数,而是小数,其他的跟randint
np.random.uniform(0, 100, (25, 4))

# .normal(loc,scale,(size)) 从指定正态分布中随机抽取样本,分布中心是loc(概率分布的均值),标准差是scale,形状是size,这个方法用的少


# .seed(s) 随机数种子,s是给定的种子值.因为计算机生成的是伪随机数,所以通过设定相同的随机数种子,可以每次生成相同的随机数
np.random.seed(10)  # 就是使用相同的随机种子之后的随机数值是一样的

# 均匀分布:在相同的大小范围内的出现概率是等可能的
# 正态分布:呈钟形,两头低,中间高,左右对称


# numpy需要注意的copy和view
# 比如 a=b 完全不复制,a和b相互影响
# a=b[:],视图操作,一种切片,会创建新的对象a,但是a的数据完全由b保管,他们两个的数据变化是一致的
# a=b.copy(),复制,a和b互不影响
