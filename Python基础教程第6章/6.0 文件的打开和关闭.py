# 通常来讲，每次运行完代码，内存数据都会释放掉，所以需要将数据存储到硬盘里，来持久的保存数据
# Python 里使用 open 内置函数打开并操作一个文件

# open 参数介绍:
# 1. file 用来指定打开的文件，不是文件的名字，而是文件的路径
# 2. mode 打开文件时的模式，默认是 r 表示只读
# 3. encoding 打开文件时的编码方式

# open 函数会有一个返回值，就是打开的文件对象
# xxx.txt 写入时，默认使用的是 utf-8 编码格式
# 在windows操作系统里，默认使用gbk编码格式打开文件,就是英文字母可以解析，但是不支持中文
# 解决方案:写入和读取使用相同的编码格式就可以了,要么改txt文件的编码格式，要么改open里的encoding,只要编码格式一致就行
file = open(
    r'C:\Users\Valentina\Desktop\python\Python基础教程第6章\xxx.txt', encoding='utf-8'
)
# print(type(file))  # <class '_io.TextIOWrapper'>
print(file.read())

file.close()  # 操作完文件以后，要关闭文件
