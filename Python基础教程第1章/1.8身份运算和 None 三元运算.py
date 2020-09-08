# 身份运算
# 查看数据类型 type()

# 如何判断数据类型，让计算机可以自动判断，然后类型
# 用身份运算来进行判断
# is , is not
name = "hello"
print(type(name) is str)  # 判断是不是字符串类型，返回 True or False
# 判断得先查看变量类型，然后在判断
print(type(name) is not str)  # 返回 is 相反的值

# None (空值，empty) 代表什么也没有
# None 的作用之一是让已经存在的变量的 值 为 None(空)

# 在没有输入变量之前，变量值为空
name = None
# 判断变量是不是为空
if name is None:
    print("你没有输入名字")
age = None
if age is None:
    print("你没有输入年龄")
height = None
if height is None:
    print("你没有输入身高")
# None 示例


# 三元运算
a = 10
b = 5
# 下面这四行代码可以改成一行代码，也就是三元运算
if a > 15:
    c = a
else:
    c = b

# 使用三元运算
num1 = 10
num2 = 5
# 上面那四行代码，用三元运算的方式写
num3 = num1 if num1 > 15 else num2
# 读取逻辑是：
# 先读取 if num1 > 15 , 如果这个条件成立 就执行 num3 = num1
# 如果 if num1 > 15 条件不成立 就执行 num3 = num2
# 就是： D = 值1 if 条件 A else 值2
# 所以如果 条件A 成立 D =值1 不成立 D=值2
# 三元运算只支持 else 不支持 elif
