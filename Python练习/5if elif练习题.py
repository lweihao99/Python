# 小王身高 1.75，体重80.5. 请根据BMI 公式(体重除以身高的平方) 帮小王计算他的BMI指数，并根据BMI指数:
# 低于 18.5 过轻
# 18.5 - 25 正常
# 25 - 28 过重
# 28 - 32 肥胖
# 高于 32 严重肥胖
# 用if elif 判断并打印结果

height = float(input("请输入你懂的身高:"))
weight = float(input("请输入你的体重:"))

BMI = weight/(height*height)
print(BMI)
# 判断你的BMI指数
if BMI < 18.5:
    print("过轻")
elif BMI >= 18.5 and BMI < 25:
    print("正常")
elif BMI >= 25 and BMI < 28:
    print("过重")
elif BMI >= 28 and BMI < 32:
    print("肥胖")
elif BMI >= 32:
    print("严重肥胖")
print("bye")
