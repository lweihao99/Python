import random  # import(导入) random 工具包

# 流程控制之 if...else..
# 单分支
age_of_Mario = 21
if age_of_Mario > 20:  # 如果变量满足条件就执行下一条代码
    print("you're old")

# 双分支
height = 180
if height > 180:  # 如果条件成立
    print("you're tall")
else:  # 如果条件不成立
    print("you're short")

# 判断你是否过了考试
vote = int(input("insert your exam vote:"))
if vote >= 60:  # 60 是及格线，过了的话就祝贺
    print("congratulation you passed the exam!!")
    print("i'm so happy for you !!!")
else:  # 如果没考过，就加油打气
    print("nevegive up!!")
    print("don't worry,you will pass it next time!!")

# 多分支 if..elif...else(可以加或者不加这个else在最后)
my_age = int(input("猜猜我的年龄:"))
if my_age < 10:
    print("哇！还是小孩呢")
elif my_age >= 10 and my_age < 18:
    print("还是青少年呢")
elif my_age >= 18 and my_age < 21:
    print("你快猜到了")
elif my_age == 21:
    print("恭喜你，猜到了")
else:
    print("我还没有那么老!")

# 多分支流程控制练习
result = float(input("enter your result:"))
if result >= 90 and result <= 100:
    print("A")
elif result >= 80 and result < 90:
    print("B")
elif result >= 70 and result < 80:
    print("C")
elif result >= 60 and result < 70:
    print("D")
else:
    print("E")

# 猜随机数
print(random.randint(0, 10))  # 随机打印 0 到 10 之间的数, randint返回(a,b)之间的随机整数
n = random.randint(0, 10)
enter = int(input("enter random number:"))  # 写出你猜想的数字
# 猜电脑给出的数
if enter > n:
    print("try smaller")
elif enter < n:
    print("try bigger")
else:
    print("got it")
