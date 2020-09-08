'''
1、编译型语言是直接将源代码编译成机器码，略过 编译，链接两个步骤 有C,C++ ， 解释型语言不需要编译，但是在运行程序的时候才逐行翻译 有 Python, JavaScript, PHP
2、Python 单行注释用 # ， 多行注释用 """aa""" 或者 ''' '''
3、布尔值(bool)分别有True and False, 就是 1 和 0
4、声明变量的时候不能用关键字， 不能用 除 字母，数字，下划线 之外的东西
5、用 TYPE(变量名) 查看变量类型
6、and 在所有条件均为 True 时，返回真
如： a= 10
b=20
b>10 and a > 10 ---> True

or 在至少一个条件为 True 时 返回 真
a> 10 or b >10 ----> False

not 返回相反的值 比如如果条件为 True 就返回 False
'''
# 7、写代码： 实现用户输入用户名和密码， 当用户名为 seven 且 密码 为 123 时， 显示 登入成功，否则失败， 失败时可以重复 3 次


count = 3
while count > 0:
    username = input("输入你的用户名:")
    password = input("输入你的密码:")
    count -= 1
    if username == "seven" or username == "weihao" and password == "123":  # 当所有条件为 True 时 打印 登入成功
        print("登入成功")
        break
    else:
        print("登入失败")

    if count == 0:
        print("你已经没有重复机会了")
