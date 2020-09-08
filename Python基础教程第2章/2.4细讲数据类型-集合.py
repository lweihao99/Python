# 集合 set
# 1、里面的元素不可变，代表你不能存一个 list or dict 在集合里， 字符串，数字，元组等不可变类型可以存
# 2、 天生去重，在集合里不能储存重复了的元素
# 3、集合是无序的，不想列表一样通过索引来标记元素在列表中的位置，元素是无序的，在集合中元素没有先后之分，比如集合{1,2,3,4,5} 和 {3,1,2,5,4}算作同一个集合
# 基于上面这些特性，集合可以用来去重和关系运算,
# 比如去重:可以将列表转化成集合，来去除重复元素


# 天生去重
a = {1, 1, 1, 1, 2, 2, 2, 3, 4, 3, 4, 5, 6, "weihao", "jack"}
print(a)
# 将列表去重,将列表转化成集合(set) 类型
q = [1, 1, 1, 1, 2, 2, 2, 3, 4, 3, 4, 5, 6, "weihao", "jack"]
a = set(q)
print(a)
print(type(a))

# set 的增删改查

# 新增,只能是不重复的元素，且是不可变
a.add("hello")
a.add(8)
a.add(("tuple1", "tuple2"))

# .discard 指定删除
# 如果这个元素存在就会将之删除，就算这个元素不存在也不会报错
a.discard(5)

# .pop 随机删除
a.pop()
# .remove 删除,跟 discard 的区别就是，如果不存在元素会报错
a.remove(3)


# 查
# 返回 bool
"tuple1" in a

# 注意 set 是不可更改的,也不能切片

# 循环,跟其他数据差不多
for i in a:
    print(i)


# 集合的关系运算

my_games = {"dota", "csgo", "league of legends",
            "assassin's creed", "warhammer", "cod", "cyberpunk 2077"}
your_games = {"csgo", "dmc", "civilization 6", "supermario's bros",
              "pokemon", "assassin's creed", "dota", "cyberpunk 2077"}

# 关系运算
# 交集 and符---> & , element in both side
print("两边都有的游戏:", my_games & your_games)
# .intersection 交集,原理同上
print("都有的游戏:", my_games.intersection(your_games))

# 并集或者合集，将两个集合合成一块 符号是----> |
print("两边的游戏合在一个集合里:", my_games | your_games)
# .union 合集，原理同上
print("所有游戏:", my_games.union(your_games))

# 差集，打印只有一个合集里有的元素， 符号---> -
print("只有my_games里有的游戏,有:", my_games - your_games)
print("只有your_games里有的游戏,有:", your_games - my_games)
# .difference 差集，原理同上
print("只有my_games集合有的游戏:", my_games.difference(your_games))
# .difference_update 是将一个集合独有的元素保留下来并重新赋值原有集合，和其他集合重复的元素被删除了

# 对称差集,删除两个集合里的共有元素 ----> ^
print("两边没有重复过的游戏有:", my_games ^ your_games)
# .symmetric_difference 对称差集，原理同上
print("没重复过的游戏:", my_games.symmetric_difference(your_games))

# 判断两个集合是不是相交，不相交，包含
# .isdisjoint 相交，判断两个集合有没有交集,返回 bool
print(my_games.isdisjoint(your_games))

# .issubset 包含，判断一个集合是不是另一个集合的子集,返回 bool
print(my_games.issubset(your_games))
# .issuperset 判断一个集合是不是另一个的父集，返回bool
print(my_games.issuperset(your_games))
