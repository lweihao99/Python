# 使用递归求 n! = n*(n-1)!
# 5! = 5*4*3*2*1 = 5*(5-1)! = 5*4*fact(3)
def fact(n):
    if n == 1:# 这里不能返回0，因为任何数*0=0
        return 1
    return fact(n-1)*n

print("阶乘是{}".format(fact(6)))


# 使用递归求斐波那契数列的第 n 个数字
# 假设 fact(6) = fact(4) + fact(5) = fact(2) + fact(3) +fact(4) + fact(5)
def fibonacci(n):
    # 在fact(2)的时候就不能往下拆了因为n-2=0但是没有第0个数
    # 所以 1+[f(2)+f(1)]+....拆到最后会发现斐波那契数列就是一堆1的相加
    if n == 1 or n == 2: # 结束递归的函数    
        return 1
    return fibonacci(n-2)+fibonacci(n-1) # 前两个数的和就是斐波那契数列

print("斐波那契数列:",fibonacci(9))