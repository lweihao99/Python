# open 参数介绍:
# 1. file 用来指定打开的文件，不是文件的名字，而是文件的路径
# 2. mode 打开文件时的模式，默认是 r 表示只读
# 3. encoding 打开文件时的编码方式

# 路径分两种:
# 1. 绝对路径:从电脑盘符开始的路径
# 2. 相对路径:当前文件所在的文件夹开始的路径


import os
print(os.sep)  # windows系统里，文件夹之间使用 \ 分隔符
# 在非windows系统里，文件夹之间使用 / 分隔
# 在Python里 \ 表示转义字符

# 绝对路径
# 路径书写的三种方式: 1. \\ 2. r'\' 3. '/' (推荐，因为每个平台都能用)
# file = open(
#     r'C:\Users\Valentina\Desktop\python\Python基础教程第6章\xxx.txt'
# )

# 相对路径,相对用的比较多，因为绝对路径不适用于所有人
# ../ ==> 返回到上一级
# ./ 可以省略不写，是表示当前文件夹
# / 不能随便用
file = open('Python基础教程第6章/xxx.txt.', encoding='utf-8')

print(file.read())

file.close()
