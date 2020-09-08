# 题目1：猜年龄游戏
# 要求：允许用户最多尝试3次，3次没猜对程序退出，如果猜对了打印恭喜并退出
import random  # 导入随机数生成工具

count = 3
n = random.randint(0, 20)  # 随机生成要猜的数字，在 0 - 20 之间

while count > 0:
    count -= 1
    # 输入你要猜的数， 这段要在循环里 因为没错一次就要从新输入一个数字
    enter = int(input("enter your number:"))
    # 判断你输入的数字是否等于系统随机生成的数字
    if enter > n:
        print("unlucky, try to enter a smaller number")
    elif enter < n:
        print("unlucky, try to enter a bigger number")
    else:
        print("congratulation, you got it !!")
        break  # 如果猜到了直接终止循环
    if count == 0:  # 当你用完机会之后
        print("unlucky, you cant try it anymore")
