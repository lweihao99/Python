# 列表是什么，就是将一大串不同的字符串储存起来，然后可以取出我需要的那个字符串
# 比如有 4 个不同的人名 但是 我需要在4个当中取出我需要的那个， 而不是全部打印出来 所以就需要列表，而不是字符串
# 比如有 100 个人名 但是 我现在需要第 50 个人的名字 把他打印出来，就不能使用 字符串， 而是列表

# 列表语法 ： names = [] , 这个是空列表
names = []
type(names)  # 类型是 list(列表)
print(names, type(names))


# 元素名 就是这些名字， 而每个元素名对应一个下标(索引)，下标是从 0 开始 每加一个元素名就 下标+1
names = ["Weihao", "Alex", "Yina", "Nion"]
print(names[2])  # 这里 下标2 对应元素名 Yina
print(names[3])
print(names[0])  # 这里由于下标是从 0 开始的 所以对应元素名 Weihao

# 对列表进行 增删改查
# 增 有 插入 和 追加

# 插入 用dot分开列表 和 他要做的事情 比如:insert(插入),  list.要做的事()
names.insert(2, "Sekiro")  # names.insert(要插入的位置,"元素名")
print(names)  # 插入到了第二个元素名的前面

# 追加会将新的元素名追加到列表的尾部
names.append("Mario")
print(names)

# 删
del names[3]  # 对应第三个元素名
del names[-1]  # 对应列表最后一个元素名以此类推
print(names)

#改 , 就是相当于从新赋值
names[-1] = "Luigi"  # 将最后一个元素名改成luigi
print(names)

# 查
print(names.index("Luigi"))  # names.index("")可以查到元素名的下标并返回
print(names.index("Weihao"))  # names.index("Weihao")  # 如果有这个元素名就会返回他的下标,反之没有
print("Weihao" in names)  # "weihao" in names  # 如过返回 true 就是有这个元素名反之没有

# 可以同时使用 del 和 names.index
# 这段代码会优先执行names.index("Alex")，并返回下标 然后 del 在删除下标对应的元素名, 这叫命令嵌套
del names[names.index("Alex")]
print(names)
