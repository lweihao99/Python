# 先让用户一次选择 6 个红球， 在选择两个篮球， 最后统一打印用户选择的球号
# 确保用户不能选择重复的，选择的数不能超出范围
'''
解题思路：
1、先规定用户能选择的数字范围，规定红球有几个，篮球有几个
2、用户每选择一个有的数字数字就提醒这是已有数字
3、用户重复输入的数字不能在输入
4。用列表来储存用户输入的数字
5、Python 运行逻辑是从上到下的
'''
# 选红球号码次数
count_red = 6
# 选篮球号码次数
count_blue = 2
listRedBallNumber = []
listBlueBallNumber = []
# 选择红球号码
while count_red > 0:
    chooseRedball = int(input("请在 0-20 之间选择你要的红球号码:"))
    if chooseRedball in listRedBallNumber:
        print("you cant choose this again!!")
        continue  # 中断单次循环，从新开始， 所以不会运行下面的计数器
    elif chooseRedball > 20 or chooseRedball < 0:  # 如果输入了范围之外的数字，就警告然后从新开始
        print("you cant choose number out of range")
        continue
    # 由于Python 运行逻辑是从上到下的 所以下面这段代码会在上面那些代码之后运行
    # 列表追加得在判断这数字是不是重复之后，要不然运行逻辑会变成每次输入一个数字之后会先存进列表里，在判断是否重复，就每次都会显示这数字已经有了
    listRedBallNumber.append(chooseRedball)
    count_red -= 1
# 选择篮球号码
while count_blue > 0:
    chooseBlueball = int(input("请在 30-50 之间选择你要的篮球号码:"))
    if chooseBlueball in listBlueBallNumber:
        print("you cant choose this number again !")
        continue
    elif chooseBlueball > 50 or chooseBlueball < 30:
        print("you cant choose number out of range")  # 输入了规定范围之外的数字，提醒并且终止单次循环
        continue

    listBlueBallNumber.append(chooseBlueball)
    count_blue -= 1

print(listRedBallNumber)
print(listBlueBallNumber)
