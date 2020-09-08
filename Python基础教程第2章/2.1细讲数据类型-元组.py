# 元组
# 语法
names = ()
print(type(names))  # tuple 类型就是 元组
# 元组跟列表的功能基本一致，除了一些小区别
names = ("weihao", "jax", "jack", "orwel")
print(names[3])
# 元组跟列表的区别就是，元组不可变,不可修改, 所以也被称之为 只读列表
# 切片和循环也跟列表一样
# 元组是可以组合的
# 示例
tuple1 = ("hello", "bye", "good")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# 删除,元祖是不允许删除元祖里的单个元素的，但是可以用 del 删除整个元组
del tuple3
# print(tuple3)  # tuple3 is not defined 被删了,打印的话会报错

# 任意无符号对象，以逗号隔开，默认为元组
a = "hello", "bye", "ciao"
print(a)

# 长度
# 返回列表或者元组的长度,返回的值是整数
print(len(names))  # 打印 4，因为元组names 只有4个元素名

# 元组本身不可变，但如果元组包含其他可变元素，那么这些可变元素可以改变
# 示例,元组包含了一个列表，列表就是一个可变元素,可修改的元素
numbers = (1, 2, 3, 4, 5, ['hello', 'weihao', 'jax'], 10)
# 将元组的第6个元素的第1个元素改掉
numbers[5][0] = 'ciao'
print(numbers)
# 为什么可以改？ 是因为元组只是存每个元素的内存地址
# 所以元组只是存了列表整体的内存地址，而列表里的元素每个是独立的，就是列表里的每个元素有它自己的内存地址，所以可以更改

games = ("cod", "csgo", "war3", "dota", ["rachel", "cat in the box", "rainy"])
games[-1][1] = "league of legends"
print(games)


# 元组内置函数
# cmp(tuple 1,tuple 2) # 比较两个元祖元素
# len(tuple) # 计算元组元素个数
# max(tuple) #返回元组中元素最大值
# min(tuple) # 返回元组中元素最小值
# tuple(seq) # 将列表转化为元组

# 适用于字典，元组，列表，字符串的方法
# 复制 *
# 复制3次
print(a*3)
