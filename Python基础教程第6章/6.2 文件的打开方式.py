# mode : 文件打开的模式
# mode 有: r, w, b
# r: 只读模式，也就是默认模式，只能读取，不能写入,如果文件不存在，会报错
# file = open('Python基础教程第6章/xxx.txt', 'r')
# print(file.read())
# file.write('hello') # 不能执行写入操作，会报错

# w: 写入模式，打开文件以后，只能写入，不能读取.如果文件存在，会覆盖文件。如果文件不存在，会创建文件
# file = open('Python基础教程第6章/xxx.txt', 'w')
# file.read() # 不能读取，会报错
# file.write('hello') # 可以执行写入的操作

# b: 以二进制的形式打开文件，可以用来操作非文本文件,比如图片
# rb: 以二进制读取， wb: 以二进制写入
# file = open('Python基础教程第6章/xxx.txt', 'rb')
# print(file.read())  # 读取的结果是二进制

file = open('Python基础教程第6章/xxx.txt', 'wb')
file.write('大家好'.encode('utf-8'))  # 没有转换会报错，只能写入二进制，就是要编码
file.close()

# 还有很多其他模式，比如:
# a: 追加模式，会在最后追加内容，如果文件不存在，会创建文件，如果文件存在，会追加，不会覆盖
# r+: 可读可写，如果文件不存在会报错
# w+: 可写可读，如果文件不存在，会创建，存在的话，会覆盖,但是最好少用r+,w+ 有很多问题
# 使用w+之后，需要将文件指针重置就是调用seek
