#题目2, 猜年龄游戏
'''
猜年龄游戏升级版
要求：
1、允许用户最多猜3次
2、每尝试3次后，如果没猜对，就问用户是否还想继续玩，如果回答 Y 或者 y,就继续让其猜3次，以此往复，如果回答 N 或者 n， 就退出程序
3、猜对了就直接退出程序
'''
import random  # 导入random 模组
count = 3  # 三次机会
n = random.randint(0, 30)

while count > 0:
    enter = int(input("enter your number:"))
    if enter > n:
        print("Unlucky, try a smaller number")
    elif enter < n:
        print("Unlucky, try a bigger number")
    else:
        print("Congratulation!!")
        print("the correct number is exactly:", n)
        break  # 猜对的话 直接退出程序
    count -= 1  # 限定循环次数
    if count == 0:  # 机会用完之后，问用户是否要继续
        answer = input("Do you wanna play again? ")  # 输入字符串
        if answer == "Y" or answer == "y":
            print("\nOk, let's do this angain")
            count = 3  # 如果玩家想继续游戏, 从新赋值成 3 继续 while 循环

        elif answer == "N" or answer == "n":
            print("cya")
            break  # 不想继续游戏的话，直接终止程序
