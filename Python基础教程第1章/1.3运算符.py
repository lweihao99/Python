# 运算符
'''
1、算术运算
2、比较运算
3、赋值运算
4、逻辑运算
'''

# 取模运算，返回除法的余数
num1 = 10
num2 = 3
print(num1 % num2)  # 10/3= 3 余 1
# 取整数
num1 = 10
num2 = 6
print(num1//num2)  # // 取除法的整数
# 幂
num1 = 2
num2 = 3
print(num1**num2)  # ** potenza(幂)， 返回x的y次幂
# 以及四则运算 + - * /

# 比较运算
num1 = 10
num2 = 16
print(num1 == num2)  # 比较两个数值是不是一样，返回 true or false
str1 = "weihao"
str2 = "Weihao"
print(str1 == str2)
print(str1 != str2)  # != 比较两个数值是不是不相等，返回 true or false
# print(num1 <> num2)  # 类似 != 比较两数是否不相等
print(num1 > num2)
print(num1 >= num2)  # 反之同样 <, <=

# 赋值运算
num1 = 50  # = 简单的赋值符
num2 = 30
num1 += num2  # 等同于 num1 = num1 + num2
print(num1)
num1 -= num2  # 等同于 num1 = num1 - num2
print(num1)
num1 *= num2  # 等同于 num1 = num1 * num2
print(num1)
num1 %= num2  # 等同于 num1 = num1 % num2
print(num1)
# 其余 如 **= , //= 原理同上

# 逻辑运算
# and 判断多个条件均为真时，返回真
num1 = 10
num2 = 20
print(num1 > 10 and num2 > 10)  # false 因为只有一个条件为 true

# or 判断多个条件任意条件为真时，返回真, 至少一个条件为 真 才返回 真
print(num1 > 10 or num2 > 10)  # true 因为有至少一个条件为真

# not 取反
print(not num1 > num2)  # num1>num2 是 false 但是not是 取反 所以打印出 true
