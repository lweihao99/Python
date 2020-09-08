# 函数,找出传入列表或元组的奇数位对应的元素,并返回一个新的列表
def funcTuple(*args):
    print("元组里所有奇数元素:", args[1::2])
    # 元组里的奇数元素赋值给 i
    for i in args[1::2]:
        # 打印奇数元素以及对应下标
        print("元素名", i, "对应下标:", args.index(i))
        # 依次打印新的列表
        newList = []
        newList.append(i)
        print(newList)
    # 在一个空列表里追加整个奇数元素元组
    entireNewList = []
    entireNewList.append(args[1::2])
    print(entireNewList)  # 打印整个新的列表
    # 转化元组为列表
    nList = list(args)
    print("整个元组转化成列表:", nList)
    # 返回一个新的奇数列表
    print(nList[1::2])
    a = nList[1::2]
    for k in a:
        print(k, "下标:", a.index(k))


# 函数调用
funcTuple(1, "Weihao", "Hello", 4, 5, 6, "Take", 8, 9, 10, 11, "Easy")


# 另一种方法

def secondMethod(con):
    # 提取技术元素并生成新的列表
    listNew = []
    for i in con:
        # 如果 i/2 余1的话就是奇数, 余0就是偶数
        if i % 2 == 1:
            # 如果是奇数就打印
            print(i)
            # 给新的列表赋值
            listNew.append(i)
    print("新的列表:", listNew)


# 函数调用
# 直接生成一系列数字,并转化成列表
secondMethod(list(range(0, 30)))
