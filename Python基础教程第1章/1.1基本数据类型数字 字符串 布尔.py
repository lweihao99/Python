"""
数字类型有:

整数
int 能储存 2**62
32
long 在Python long 能储存的数字是无限大, 不过在 Python 3 里 所有的整数都按 int 处理， 不在有 long

浮点数/小数
float 
3.14159

"""
age = 21
type(age)  # type 是用来查看这个变量是什么数据类型
print(age, type(age))

pai = 3.14159
type(pai)
print(pai, type(pai))  # 在 Python 不用先定义是什么类型的数据，所以Python 是弱类型语言，反之如 C++ ，C 的语言是强类型

"""
字符串类型:
不用如 C++ 一样先定义类型
Python 的字符串语法:
    name="weihao" 有引号就是字符串
"""

name = "weihao"  # 双引号和单引号在使用上没有区别
print(name)

name = "i'm weihao"  # 这里单引号和双引号的用来区分，是一种比较普遍的用法

name = '''my name\n is\n weihao '''  # 三引号是用来写多个段落/多行的

setence1 = "我本将心向明月"
setence2 = "无奈明月照沟渠"
print(setence1+setence2)  # 字符串可以拼接
print(setence1*3)  # 可以直接打印三次字符串
# print(setence1*setence2) 这种事错误写法

# 布尔类型
a = 5
b = 4
print(a > b)  # 如果成立为 真 不成立为 假， true(1) or false(0)
