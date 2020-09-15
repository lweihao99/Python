import numpy as np

t = np.arange(24).reshape(2, 12)
print(t, "\n")
# 获取最大值最小值的位置
# 1.
print(np.argmax(t, axis=0), "\n")  # axis=0 代表取每一列的最大值的位置
# 2.
print(np.argmin(t, axis=1), "\n")  # axis=1 代表取每一行的最小值的位置

# 创建一个全为0的数组
print(np.zeros((3, 4)), "\n")  # 传一个元祖,里面的是行数和列数

# 创建一个全为1的数组
print(np.ones((3, 4)), "\n")  # 元祖里的是行数和列数

# 创建一个对角线为1的正方形数组(方阵),除了对角线为1其他全为0
print(np.eye(3), "\n")
