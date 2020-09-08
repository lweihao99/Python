# 在0-1之间随机添加点,算出一个圆圈的pi
# https://www.youtube.com/watch?v=pvimAM_SLic&ab_channel=JomaTech,可以看题目,以及解题思想
import random


def estimate_pi(n):  # n = 点数
    num_point_circle = 0  # 初始化在圆圈里的点数
    num_point_total = 0

    for i in range(n):  # 遍历每一个点
        # x -- 随机数的最小值，包含该值,y -- 随机数的最大值，不包含该值
        # uniform方法，将在x,y范围内随机生成一个实数，返回值是浮点数,如果 x<y 则 x <= N <= y，如果 y<x 则y <= N <= x
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2  # x^2 + y^2 = r^2

        if distance <= 1:  # 判断点是不是在圆圈的范围里,因为 r = 1
            num_point_circle += 1
        num_point_total += 1

    # pi*r^2/(2*r)^2 = num pt circle/num pt total
    return 4*num_point_circle/num_point_total


print(estimate_pi(100000))  # 数值越大越准确,pi = 3.14159265359
