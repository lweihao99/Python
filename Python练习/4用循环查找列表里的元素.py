# 当列表的元素很多的时候如何灵活的运用 for 循环查找我要的数据
list_memberInfo = [["Weihao", "student", "5000"], ["Elena", "student", "4000"], ["Francesca", "dancer", "4000"], [
    "Betty", "teacher", "3500"], ["Liu", "Game designer", "8000"], ["Jessy", "singer", "10000"]]

# 用循环查找 Liu 的职业
# 赋值临时变量 i 列表里的元素(小列表)
for i in list_memberInfo:
    # 如果在小列表里有 "Liu" 这个元素就打印出他的职业信息
    if "Liu" in i:
        print(i[1])

# 这就是如何使用for 循环在一个大的列表里指定查找某个信息
# 但是比起使用字典效率非常低
