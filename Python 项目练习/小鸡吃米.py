# @author: Andersen
import random
# 分数
score = 0
# 游戏提示
print("WASD为移动方式;'+'代表你的当前位置,'*'代表目标位置;quit退出游戏！")
print("游戏开始！！！")
userX = 0
userY = 0
targetX = random.randint(0, 9)
targetY = random.randint(0, 9)
# 永远再循环,每次循环刷新一下玩家的位置
while True:
    # x 轴
    for one in range(0, 10):
        xz = ""
        outStr = ""
        # y 轴
        for two in range(0, 10):
            if userX == targetX and userY == targetY:
                targetX = random.randint(0, 9)
                targetY = random.randint(0, 9)
                score += 1
                print("当前分数:%d" % (score))
            # one=x轴, two=y轴,玩家的位置显示为 +
            if userX == one and userY == two:
                xz = "+"
            # 目标位置显示为 *
            elif targetX == one and targetY == two:
                xz = "*"
            # 其余不是玩家或目标的位置都显示为 -
            else:
                xz = "-"
            # 将各自的符号从新赋值
            outStr += xz
        # 打印各自的位置
        print(outStr)
    # 玩家的行动方式
    move = input("请移动或退出：").upper()
    if move == "QUIT":
        break
    elif move == "S" and userX < 9:
        userX += 1
    elif move == "W" and userX > 0:
        userX -= 1
    elif move == "D" and userY < 9:
        userY += 1
    elif move == "A" and userY > 0:
        userY -= 1
    # print(move)
print("游戏结束，最终得分：{}".format(score))
