
# *函数的返回值
# 概念:函数执行完以后会返回一个对应对象,如果在函数的内部有 return 的关键字就可以返回实际的值,否则会返回 None
# 类型:可以反回任意类型,返回值类型应该取决于 return 后面的类型
# 用途:给调用方返回数据
# 在一个函数体内可以出现多个 return 值:但是肯定只能返回一个 return
# 如果在一个函数体内,执行了return, 意味着函数执行完成退出了, return 后面的代码语句将不会执行
# 语法结构:

def Sum(a, b):
    sum = a+b
    return sum  # 将计算结果 sum 返回到调用, 将函数的处理结果返回了
    # 返回值类型取决于return 后面的变量


print(Sum(20, 20))  # 输出函数的返回值
print("分割线".center(50, "-"))
# 或者


def Sum1(a, b):
    sum = a+b
    return sum  # 将计算结果返回


data = Sum1(10, 10)  # 将返回值赋给其他变量
print(data)
print("分割线".center(50, "-"))
# 查看返回值的数据类型


def calComp(num):
    li = []
    result = 0
    i = 1
    while i < num:
        result += i
        i += 1
    li.append(result)
    return result  # 返回值将返回到调用


# 输出返回值
value = calComp(10)
print(value)
print(type(value))  # 这里返回的类型是 整型 int,以为这查看的类型是返回值就是 return 后面的变量类型
print(calComp(5))
print(type(calComp))  # 这里返回的类型是 函数 function, 这里查看的类型是函数调用
print("分割线".center(50, "-"))
# 返回列表


def calComp1(num):
    li = []
    result = 0
    i = 1
    while i < num:
        result += i
        i += 1
    li.append(result)
    return li  # 返回值将返回到调用


value1 = calComp1(15)
print(value1)
print(type(value1))  # 这里的类型是 list 因为 return 后面的变量是 list 类型
print("分割线".center(50, "-"))
# 返回元组


def tupleTest(*args):
    return args


value2 = tupleTest("返回值类型为 tuple", 20, "Tuple", "Tuple 1", "Hello", 1)
print(value2)
print(type(value2))
print("分割线".center(50, "-"))
# 或者不用参数来返回元组


def tupleTest2():
    return 1, 2, 3  # 直接在 return 后面写, 不用参数


Tup = tupleTest2()
print("不写参数返回的数据类型:", type(Tup))
print("不用参数,直接在 return 后面写的值:", Tup)
print("分割线".center(50, "-"))
# 返回字典


def Dict(**kwargs):
    return kwargs


# 将调用(返回值)赋值给新的变量
value3 = Dict(type="返回值类型为字典", name="Weihao")
print(value3)
print(type(value3))
print("分割线".center(50, "-"))

# 不用参数来返回字典


def DictFunc():

    return {"name": "weihao", "age": 21}  # 必须用字典格式写


# 将调用(返回值)赋值给新的变量
dictF = DictFunc()
print("不用参数,直接在 return 后面写的值:", dictF)
print("不写参数返回的数据类型:", type(dictF))
print("分割线".center(50, "-"))

# 所以可以根据需要直接在 return 后面根据你写的格式,返回你需要的数据类型


# *函数的嵌套调用
# 概念:函数的嵌套调用就是在函数内部调用另外一个函数
# 内层函数可以访问外层函数中的定义变量,但不能从新赋值(rebind)
def function1():
    print("开始函数function 1".center(50, "-"))
    print("执行function 1代码区间".center(50, "-"))
    print("结束函数function 1".center(50, "-"))


def function2():
    print("开始第二个函数".center(50, "-"))
    # 调用第一个函数
    function1()
    print("结束第二个函数".center(50, "-"))


# 调用 function2
function2()
# 所以运行逻辑是，先运行调用函数(function2)--->运行第一行代码 --->遇到 function1 的函数调用--->运行 function1---->继续运行函数2(function2)


# *函数的4种基本类型
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
