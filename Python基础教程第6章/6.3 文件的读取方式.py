# python 里使用 open 内置函数用来打开一个文件
# file: 文件路径 ==> 相对路径和绝对路径
# mode: 打开文件的模式 ==> r:只读, w:写入, b:二进制, t: 文本形式打开
# mode 默认的打开方式是rt
# encoding: 用来指定文件的编码方式，windows默认是 gbk

# file = open('Python基础教程第6章/xxx.txt')  # 默认是rt打开.如果文件不存在，会报错

# file = open('./sss.txt', 'w', encoding='utf-8')  # 创建一个新的文件
# file.write('你好')

file = open('./xxx.txt', encoding='utf8')

# file.read()  # 读取所有数据
# file.readline()  # 读取单行数据

# while True: # 逐行读取出来
#     content = file.readline()
#     print(content)
#     if content == '':
#         break

# x = file.readlines()  # 将所有的数据都读取，保存到一个列表里
# print(x)

# 使用read可以指定读取的个数，大小，用的最多的方法,这种方法在读取大型文件的时候可以节省电脑资源，不会一次性读取所有数据，不然会给电脑造成很大的压力
file.read(1024)

# 在开发的时候没有绝对的优化，除非提升硬件
# 软件层面的优化是时间换空间，或者空间换时间，
# 比如要想快速的读取一个大型文件，那么就要一次性就读取很大的数据，这会很耗电脑的资源，反之如果一点一点的读取数据虽然消耗的时间会变长，但是消耗的电脑资源会变少

# 缓存就是保存一个数据在某个地方，每次用户需要的时候就调用，用来节省时间

# 需要注意的是，读取一个非文本文件需要使用rb，也就是用二进制来读取

file.close()
