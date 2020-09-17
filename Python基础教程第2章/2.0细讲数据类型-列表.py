# 储存元素名
# names = ["weihao", "jone", "jack"]
# # 索引下标来打印我需要的值
# # 下标从0开始，对应列表里的第一个元素名
# print(names[1])  # 数字是下标,这里是 jone

# # 列表特点
# # 1、可多放多个值
# # 2、按照从左到右的顺序定义列表元素，下标从0开始顺序访问，是有序的
# # 3、可修改指定索引位置对应的值，可变

# # 追加
# enter = input("enter what you want: ")
# name = []
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# name_list = ["weihao", "jax", "kack", "jack", "william"]
# # 追加 enter 输入的值到 name 空列表里

# name.append(enter)
# print(name)

# # 插入
# name_list.insert(3, enter)
# name_list.insert(4, "god")

# # 合并
# name_list.extend(number_list)  # 将两个列表合并在一起
# print(name_list)

# # 列表嵌套
# # 插入是在列表里插入一个值，而列表嵌套是在列表里嵌套列表
# name_list.insert(0, [1, 2, 3])
# # 打印出插入到0下标的列表的第二个元素名
# print(name_list[0, 2])  # 打印出 2

# # 删除操作
# # del 删
# del number_list[0]
# print(number_list)  # 这里元素1被删了

# # .pop 删
# number_list.pop()  # 默认功能，默认删除最后一个元素，并返回被删除的值
# print(number_list)  # 这里最后一个数字被删了

# number_list.pop(3)  # 删除指定元素,并返回删除值
# # 列表为空的时候会报错

# # .remove删除从左到右第一个匹配的元素
# # 如果有多个同样的元素 .remove 会删掉第一个遇到的那个
# # 如果要 .remove 一个不存在的元素将会报错
# name_list.remove("jax")

# # clear 清空
# names.clear()  # 直接清空整个列表
# print(names)

# # 修改操作
# games = ["cod", "battlefield", "dota", "csgo"]
# games[0] = "leagueOfLegends"  # 修改第0个元素的值
# games[-1] = "cyberpunk 2077"  # 修改倒数第一个元素的值

# # 查操作

# # .index 如果查看一个没有的元素就会报错
# # .index 不能查看嵌套在列表里的数据
# # 语法: 变量名.index(value,start,stop), star 就是开始索引，默认为 0, stop 就是结束索引，默认为字符串的长度
# # 返回从左开始匹配到第一个 dota 的索引，就是返回元素的下标
# print(games.index("dota"))  # 返回 2

# # .count 如果查看没有的元素会返回 0
# # # 返回 dota 的个数
# print(games.count("dota"))  # 返回 1

# # 判断列表里有没有我要的元素
# print("battlefield" in games)  # 返回 True 就是有 is not 来反转返回值


# 列表切片
# 作用：同时取出元素的多个值
# 语法: 变量名[start:end],取出start的元素到end的元素，但不包含end本身
champion = ["aatrox", "ezreal", "nami", "garen", "yasuo"]
print(champion[1:4])  # 打印 ezreal,nami,garen
# 可以倒着切，方便取出倒数最后一个（当一个列表元素太多的时候）,但要记住最后一个元素是不会被取出来的
print(champion[0:-1])
# 如果想要取出从start到列表最后一个元素
print(champion[1:])  # end 不写可以取出从 ezreal 到 yasuo 的所有元素，包含yasuo
# 同理如果start 不写的话就代表从0开始
print(champion[:4])
# 倒着切
print(champion[-5:-1])
# 不是从右往左，会报错
# 所以如果写 champion[-1:-5]会显示空列表

# 步长(步子的长度)
# 在切片的时候，默认步长是1,而用步长可以改变这个长度,使切片可以跳着切
#语法是: 变量[start:end:步长]
print(champion[0:4:1])  # 步长1, 每次迈一步
print(champion[0::2])  # 步长2, 每次迈两步，打印:aatrox,nami,yasuo
# 如何使列表真正的倒着切
# 就是灵活使用步长
print(champion[-1:-5:-1])  # 打印: yasuo,garen,nami,ezreal
# 步长为 -1 就可以打印出从右到左的列表
# 同时步长 -1 可以反转值
a = "alyx"
print(a[::-1])  # 打印 xyla , 在没有用.reverse 使用步长 -1 的情况下反转了字符串


# 列表循环和排序
# 列表反转功能 .reverse
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# .reverse 会把原列表也反转过来
num.reverse()
print(num)

# 排序
Text = ["2", "@", "%", "hello", "eve", "ace"]
# 排序顺序逻辑,是按照字符编码表顺序来排序的
# 要注意数字和字符串不能直接排序比较
Text.sort()
print(Text)


# 循环列表
# 使用 for 循环
for i in Text:  # i 是临时变量
    # 如果 临时变量 i == "hello", 就打印 "ciao"， 也就是所当 i == hello 的时候,将不会打印 hello 而是会打印 ciao
    if i == "hello":
        print("ciao")
    # 反之就正常打印 i, 也就是依次打印 Text 列表里的元素名
    else:
        print(i)
# 每次循环，Text 列表里的元素就会依次赋值给临时变量 i,然后在依次打印 i
