# 找到文件并打开 open
# 变量名 = open(filename)

# 读文件 .read
# 变量名.read(100)读100个字符, .read()读所有

# 写文件 .write
# 变量名.write(yourData)

# 保存,关闭
# .close()自动保存并关闭


# *文件打开模式
# Python 只能以一种模式操作文件，比如只能读不能写，反之亦然，不能混着操作
# 操作模式有3种:
# r ---> read
# w ---> write 创建模式，创建一个新的文件，如果这个文件已经有了，就会将原有的内容清空，并用新的内容覆盖掉
# a ---> append

# *# 选定目录，创建模式
# f = open(file='C:/Users/WEIHAO/Desktop/学校以及其他/universita/test.txt', mode='w')
# # 写文件
# f.write("测试使用Python创建新文件\n")
# f.write("hello hello ciao ciao ciao hello hello world")
# f.close()


# *# 只读模式
# f = open(file='C:/Users/WEIHAO/Desktop/学校以及其他/universita/test.txt', mode='r')
# print(f.readline())  # 读一行
# print("分隔符".center(50, "-"))

# data = f.read()  # 读所有,剩下的所有
# print(data)
# f.close()
# 只读模式是不能写的


# *追加模式
f = open(file='C:/Users/WEIHAO/Desktop/学校以及其他/universita/test.txt', mode='a')
f.write("\nbabyboyrunningboy helllllo\n")  # 这一行会追加到文件尾部
f.close()  # 关闭并自动保存
