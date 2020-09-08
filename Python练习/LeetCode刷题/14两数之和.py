# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
numberList = [2, 7, 11, 15]
target = 9
# 总和 = target 数组列表
totNum = []
# 取模值为0 的数组列表
newList = []
newList1 = []
# 存取数组下标的列表
underNum = []

# 设两个变量，是他们相加，如果总和为target 的值就打印对应元素
# 循环第一个变量
for i in numberList:
    # 循环第二个变量
    for k in numberList:
        # 两个变量相加
        summs = k+i
        # 判断总和值是不是 = target，如果符合条件就打印符合条件元素的下标
        if summs == target:
            totNum.append(k)
            # 数组下标
            underNum.append(numberList.index(k))

        # 如果总和值除以 target 的余等于 0, 就
        if summs % target == 0:
            newList.append(k)
            newList1.append(summs)

print("组合起来可以取模0的值:", newList)
print("总和可以除以9的值:", newList1)
print("数组相加相等于9的值:", totNum)
print("那些相加 = 9 的数组下标:", underNum)
