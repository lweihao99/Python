# 针对列表 names = ["金角大王","黑姑娘","rain","eva","狗蛋","银角大王","eva","鸡头"] 进行以下操作:
# 1、通过 names.index() 返回第二个 eva 的索引值
# 2、把以上列表通过切片的形式实现反转
# 3、打印列表中所有下标为奇数的值
# 4、通过 names.index() 找到第2个 eva 值，并将其改成 EVA

names = ["金角大王", "黑姑娘", "rain", "eva", "狗蛋", "银角大王", "eva", "鸡头"]
# 1、用 .index 返回第二个 eva 的下标
print(names.index("eva", 4, 7))  # 返回下标 6
# 2、切片反转
print(names[::-1])
# 3、打印列表中所有下标为奇数的值
print(names[1::2])
# 4、找到第2个 eva 并将其改成 EVA
names[names.index("eva", 4, 7)] = "EVA"
print(names)

games = ["MineCraft", "Dota", "LeagueOfLegends",
         "Cod:Modern Warfare", "CSGO", "Valorant", "PUBG"]
for i in games:
    # 如果 i == valorant 就打印 csgo is better, im joking :)
    if i == "Valorant":
        print("csgo is better, im joking :)")
    # 循环打印 games 列表的元素名
    else:
        print(i)
