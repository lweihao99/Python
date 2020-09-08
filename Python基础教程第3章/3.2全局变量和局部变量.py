# 函数的4种基本类型
"""
1、无参数，无返回值，一般用于提示信息打印
def myprint():
    print("-"*20)
    
2、无参数，有返回值，多用在数据采集中，比如获取系统信息
def mycpu():
    #获取cpu信息
    return info

3、有参数，无返回值，多用在设置某些不需要返回值的参数设置
def set(a):
    pass

4、有参数，有返回值，一般是计算型的，需要参数，最终也要返回结果
def cal(a,b):
    c = a +b
    return c
"""

# *局部变量


def printInfo():
    # 在函数中定义变量
    name = "Weihao"
    print("{0}".format(name))
    pass


# 调用函数
printInfo()


# def testMethod():
#     # name是局部变量，变量的作用域只有在函数printInfo内 ，不能影响到函数外，所以这里打印不出 name,除非在这个函数里也定义一个name函数
#     # 局部变量哪怕同名也不会影响到彼此，因为只在函数内部生效
#     print(name)
#     pass


# # 调用函数
# testMethod()

# 局部变量的作用是为了临时的保存数据，需要在函数中定义来进行存储，因为一但函数执行完了里面的代码就失去了意义了

# *---------------------------------------------------分割线-------------------------------------------------------

# *全局变量
# *如果局部变量跟全局变量名称相同，函数会优先使用局部变量，对函数来说局部变量优先级更高

pro = "designer"  # 全局变量能影响到整个文件，所有函数都能引用
name = "jacky"


def infoPoint():
    name = "Weihao"
    print("{0},{1}".format(pro, name))


# 函数调用
infoPoint()


def secInfoPoint():
    print("{0}".format(pro))


# 函数调用
secInfoPoint()


# 使用函数修改全部变量
def changeGlobal():
    """
    修改全局变量
    """
    # pro = "pro gamer"  # 这是局部变量
    # *想要修改全局变量需要用关键字 global
    global pro
    pro = "pro player"  # 修改全局变量


# 函数变量
changeGlobal()

print("修改之后的全局变量:", pro)
