# 1函数,接收 2 个数字,求这些参数数字的和，用返回值 return 的方法
def Sum(a, b):
    sum = a+b

    return sum


# 函数调用
print("用return的方法")
cal = Sum(a=int(input("first number:")), b=int(input("second number:")))
print("数字总和为:", cal)
print("万能分割线".center(50, "*"))

# 2函数,接收 2 个数字,求这些参数数字的和


def Sum1(a, b):
    sum = a+b

    print("不用return直接在代码里输出:", sum)


# 函数调用
print("不用return的方法")
Sum1(a=int(input("enter 1st number:")), b=int(input("enter 2nd number:")))
print("万能分割线".center(50, "*"))

# 3函数,接收 n 个数字,求这些参数数字的和


def second(*args):
    # 给个初始值
    result = 0
    # 累计
    for i in args:
        result += i

    print("总和:", result)


# 函数调用
second(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("万能分割线".center(50, "*"))
print("万能分割线".center(50, "*"))

# 4用 return


def second(*args):
    # 给个初始值
    result = 0
    # 累计
    for i in args:
        result += i

    return result


# 函数调用
a = second(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("总和:{0}".format(a))
