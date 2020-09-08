import random


# 编写一个函数，求多个数中的最大值

# def getMax(*args):
#     num = args[0]
#     for item in args:
#         if item > num:
#             num = item

#     return num


# x = getMax(1, 2, 3, 4, 5, 6, 8, 5, 7, 98, 67, 67)
# print(x)

# 优化上面的代码


def Max(*args):

    return max(args)


print(Max(1, 32, 12, 3, 2, 31, 2123, 3))

# 编写一个函数，实现骰子的功能，打印N个骰子的点数和

# 方法1


# def All():
#     enter = input("开启骰子，输入yes or no:")
#     if enter == "yes":
#         count = 6
#         n = 0
#         i = 0
#         while count > 0:  # 限制次数

#             rand = random.randint(1, 6)  # 随机数
#             x = rand
#             n += x  # 求每个数的和 n = n + rand, 就是前两个的和加新的数值
#             count -= 1
#             i += 1
#             print("第%d随机数" % (i), rand)

#         return n

#     elif enter == "no":
#         print("程序已关闭")
#         exit(0)
# print(All())

def Sum(n):  # n个骰子的数的和
    m = 0
    i = 0
    for i in range(n):
        x = random.randint(1, 6)
        m += x
        i += 1
        print("第%d个随机数" % i, x)

    return m


print(Sum(6))


# 编写一个函数，提取指定字符串中所有的字母，然后凭借在一起产生一个新的字符串

def getAlpha(word):
    newStr = ''
    for i in word:  # 判断单个字符是否符合标准
        if i.isalpha():  # .isalpha方法 就是判断这个字符串是否是纯字母组成，如果是就返回True 否则 返回 False

            newStr += i

    return newStr


print(getAlpha('wei3123sda23;[sd/.'))

# 写一个函数，求多个数的平均值


def getSum(*args):

    m = 0
    for item in args:
        m += item

    return m / len(args)


print(getSum(1, 2, 3, 4, 5, 6))


# 写一个函数，默认求10的阶乘，也可以求其他数字的阶乘


def getFactorial(n=10):

    if n == 1:
        return 1
    return getFactorial(n-1)*n  # 这里由于函数里是 n-1 所以返回的时候替换了原先的n

# 求阶乘的另一种方法
# def getFactorial(n=10):
#     m = 1
#     for i in range(1, n+1):
#         m *= i

#     return m


print(getFactorial())


# 写一个自己的capitalize函数，能够指定字符串的首字母变成大写字母

# def getCapitalize(word):

#     return word.capitalize()

# 另一种写法，使用切片


def getCapitalize(word):
    c = word[0]
    if 'a' <= c <= 'z':  # 判断首字母是不是字母
        new_str = word[1:]  # 除第一个字母都要
        return c.upper()+new_str  # upper 是将所有字母大写
    return word


print(getCapitalize('123come hello'))


# 写一个自己的endswith函数，判断一个字符串是否以指定的字符串结束

# def my_endswith(old_word, new_word):
#     c = old_word[len(old_word)-1:]
#     s = new_word[len(new_word)-1:]
#     if c == s:
#         return "True"
#     else:
#         return "没有以指定字符串结束"

# 优化上面的代码


def my_endswith(oldWord, newWord):
    return oldWord[-len(oldWord):] == newWord

# 使用endswith 方法


# def my_endswith(word):
#     if word.endswith('ao'):
#         return 'True'
#     else:
#         return 'False'


print(my_endswith('weihao', 'weiha'))


# 写一个自己的isdigit 函数，判断一个字符串是否是纯数字字符串

def my_isdigit(oldStr):
    for item in oldStr:
        if not '0' <= item <= '9':  # 判断非数字
            return False
    return True

    # def my_isdigit(number):
    #     return number.isdigit()
print(my_isdigit('012gh'))


# 写一个自己的upper函数，将一个字符串中所有的小写字母变成大写字母
# a ==> 97 A ==> 65 差别是32
def my_upper(word):
    newStr = ''  # 拼接用的
    for item in word:
        if 'a' <= item <= 'z':
            # ord方法转变字符串成对应的ASCII码, chr是转变integer为字符串(string)
            upper_item = chr(ord(item)-32)
            newStr += upper_item
        else:
            newStr += item
    return newStr


print(my_upper('Wor23dsdq'))


# 写一个自己的rjust函数，创建一个字符串的长度是指定长度，原字符串在新字符串中右对齐，剩下的部分用指定的字符填充

def my_rjust(word, long):
    c = len(word)
    char = '+'
    if c != long:
        a = long - c
        return char*a + word


print(my_rjust('hell', 7))


# 写一个自己的index函数，统计指定列表中指定元素的所有下标，如果列表中没有指定元素返回-1

def my_index(*args):
    search = 'a'
    count = 0
    index_number = []
    while count < len(args):
        for item in args:
            if search == item:
                index_number.append(count)
            count += 1
    if search not in args:
        return '-1'

    return index_number


print(my_index('a', 'b', 'c', 'd', 'a', 'a', 'z'))


# 写一个自己的len 函数，统计指定序列中元素的个数

def my_len(*args):

    count = 0
    for item in args:
        count += 1
    return count


print(my_len(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'asd', 'wqe', '1'))


# 写一个函数实现自己的in操作，判断指定序列中，指定元素是否存在

def my_in(*args):
    item = 1
    for i in args:
        if item == i:
            return True
    return False


print(my_in(1, 2, 3, 'hello'))


# 写一个自己的replace函数，将指定字符串中指定的旧字符转化成指定的新字符串

# def my_replace(allStr, oldStr, newStr):

#     return newStr.join(allStr.split(oldStr))  # 用split方法分段,然后用join方法拼接

# 另一种方法

def my_replace(allStr, oldStr, newStr):
    result = ''  # 保存结果，由于字符串是不可变的，旧的不能删改，所以得加新的进去就得拼接
    i = 0
    while i < len(allStr):
        temp = allStr[i:i+len(oldStr)]  # 每次切要修改的字符串长度，并且比较
        if temp != oldStr:
            result += allStr[i]  # 每次加一个,防止切断后面的字符串
            i += 1
        else:  # 当 字符串一样的时候
            result += newStr  # 添加newStr的字符串来替换原先的字符串
            i += len(oldStr)  # 直接跳3格，因为oldStr 的字符串是长度为3

    return result


print(my_replace('how are you? and you', 'you', 'me'))


# 写一个自己的max函数，获取指定序列中元素的最大值，如果序列是字典，取字典的最大值

def my_max(iterab):
    # if isinstance(iterab,dict) # 看对象iterab 是否是通过dict类创建出来的实例
    if type(iterab) == dict:  # 判断是不是字典
        iterab = list(iterab.values())  # 将values的值取出，并赋值给iterab, 转化成列表的形式
    x = iterab[0]
    for i in iterab:
        if i > x:
            x = i
    return x


print(my_max([1, 2, 3, 4]))


# 写四个函数，分别实现求两个列表的交集，并集，差集，补集的功能

# 交集
def intersection(list1: list, list2: list):
    newList = []
    for i in list1:
        if i in list2:
            newList.append(i)
    return newList

# 并集


def union_set(list1: list, list2: list):

    return list(set(list1 + list2))  # 集合自带去重

# 差集


def difference(list1: list, list2: list):
    newList = []
    for i in list1:
        if i not in list2 and i not in newList:
            newList.append(i)
    return newList

# 对称差集，删除两个集合里的共有元素


def symmetry_diff_set(list1: list, list2: list):
    newList = []
    for i in list1+list2:
        if (i in list1 and i not in list2) or (i not in list1 and i in list2):
            newList.append(i)

    return newList


print(intersection([1, 2, 3], [2, 4, 6]))
print(union_set([1, 2, 3, 3], [3, 4, 5, 6]))
print(difference([1, 2, 3, 4], [1, 3]))
print(symmetry_diff_set([1, 2, 3, 6, 7], [1, 2, 3, 4]))
