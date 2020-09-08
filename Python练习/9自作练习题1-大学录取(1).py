# 输入你想要上的大学
# 可以上的大学写到元组里 3个，因为不能更改
# 设3个分数线，分别上3个不同的大学, 每个大学只有一个名额
# 及格线60分
# 分别写3次分数

# 能选的大学,不能修改
university = ("清华大学", "米兰理工大学", "Biccoca")
university_choose = []
# 大学的三个名额
count = 3
# 选择大学
while count > 0:
    vote = int(input("请输入你的分数:"))
    # 判断分数线是否及格
    if vote >= 60:
        print("恭喜你，及格了!")
        choose_uni = input("请在清华，米兰理工，Biccoca里选择你想上的大学:")
        # 判断大学是否已被选取，以及输入心仪大学
        if choose_uni not in university_choose and choose_uni in university:
            print("很好，你选择了 ", choose_uni, " 请尽快前去大学报到")
        elif choose_uni in university_choose:
            print("很抱歉这所大学已被选定，你已不能再选!")
            continue
        university_choose.append(choose_uni)
    # 通知没通过考试的，并且终止单次循环
    else:
        print("很抱歉，你没有通过录取考试，请你再接再厉~")
        continue
    # 打印选取大学
    print("已被选中大学列表:", university_choose)
    count -= 1

# 打印选取大学下标
for i in university_choose:
    print(i.strip(), "的下标为", university_choose.index(i))

# 打印每位学生分别选了那座大学
num = 0  # 每位学生对应编号
for k in university_choose:
    num += 1
    print("student", num, "choose: ", k)
