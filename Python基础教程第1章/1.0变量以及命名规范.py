print("hello world")
"""print 就是打印 双引号里的内容 """
print("hello your sister")

'''变量'''
Number1 = 10  # 先定义变量, 变量是分一个内存空间在给它命名（就是所谓的变量名），就是给一段内存空间然后储存进去
Number2 = 2
print(Number1*Number2)  # 在定义了变量之后 用代码调用变量，运算是由CPU负责的

name = "炜豪"  # 变量名只能是 字母 数字 下划线 的任意组合, 不能以数字开头， 以及不能使用关键字就是语法
surname = "刘"
age = 21
print(name, surname, age)

AgeOfMine = 21
print(AgeOfMine)  # 这是一种叫做驼峰体的命名方式，多用于Java 和 C， Python 尽量用下划线命名

Age_of_mine = 21
print(Age_of_mine)  # 下划线命名方式，多用于 Python

# Python 不同于 C 或者 C++ 没有专门定义常量的代码, 只能从变量名上提示这个变量是常量
NAME = "炜豪"  # Python 通常用大写来表示这个变量是常量，但从程序上来讲这只不过是一个普通的变量
print(NAME)
