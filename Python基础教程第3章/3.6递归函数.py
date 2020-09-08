'''递归函数的定义：
递归函数是函数在内部不调用其他函数，而是调用自己本身，这个函数就是递归函数

#递归函数必须满足的条件：
    1，必须满足一个结束条件，否则会无限循环下去，递归下去
    2，必须要有一个出口，比如return，就是不许要有一个明确的结束条件
# 优点：
    1，逻辑简单
    2，定义简单
# 缺点：
    1，容易导致栈溢出，就是内存资源过度消耗，内存资源紧张，甚至内存泄漏

# 递归函数的调用过程是逐阶往下的,然后返回的值是逐阶往上的,详情看下面例子

'''
# 例子1
def func(n):
    if n==1: # 满足条件就返回1
        return 1 # 当函数的值到达1的时候就会返回然后逐阶往上
    return n*func(n-1) # 递减到0的时候跳出循环
    '''
    调用过程是: 进去的时候是5然后-->4*func(3)-->3*func(2)-->2*func(1)
    而到了底部的时候就会返回1-->返回2-->返回6-->返回24-->最终返回120 就是5!的结果
    '''
#递归调用
print("使用递归函数{}".format(func(5)))

# 而使用常规的循环方法
def fact(n):
    result = 1
    for i in range(1,n+1): # 使用breakpoint 可以逐行运行程序
        result*=i

    return result

#调用函数
print("5! = {}".format(fact(5)))

# 递归函数的案例
# 模拟文件的查找，树形结构的遍历
import os # 文件操作模块
def findFile(filePath):
    listRs = os.listdir(filePath) # 获取该路径下面所有的文件和文件夹
    # 遍历得到的文件夹
    for i in listRs: # 给 i 赋值遍历出来的文件名
        full_path = os.path.join(filePath,i) # 组合成完整文件路径,使用拼接的方式将路径拼接在一起
        if os.path.isdir(full_path): # 判断是不是文件夹 
            # 如果是文件夹，就调用函数
            findFile(full_path) # 将遍历出来的文件路径导入进去 # 如果是一个文件夹，再次去递归
        else:
            print("这是文件:",i) # 如果不是文件夹直接打印文件
    else:
        return 

    pass

# 调用搜索文件夹对象
findFile(r'C:\Users\Valentina\Desktop\python\xls文件')

# 递归函数原理
# 在一个函数里可以调用另一个函数，所以也就可以自己调用自己
# 递归简单来说就是函数内部自己调用自己
def test():
    print("test")
    test()


def demo():
    print("demo")

count = 0
def tell_story():
    global count
    count +=1
    print("{}-从前有座山".format(count))
    print("山上有座庙")
    print("庙里有个老和尚")
    print("还有一个小和尚")
    if count<5:
        tell_story()

tell_story() # 调用函数
# 这里开始调用然后在函数内部有重复的继续调用，就会形成一个循环,一直输出函数内容,顺序从上往下,直到递归到程序崩溃
# 所以为了结束递归，需要找到一个出口，就是一个停止条件, 比如添加一个计数器count


# 求 1~n的和
# 比如 1+2+3+4+5+6 = get_sum(5)的和 + 6 = get_sum(4)的和 + 5 + 6...
# 就相当于 get_sum(num-1)+n
# ...get_sum(0)+1...+6-->当判断num==0的时候返回0作为结束条件
# 意思就是get_sum(0)==0，就是直接告诉你这个结果就是0所以不再递归了
def get_sum(num):
    if num == 0:# 结束递归的条件
        return 0 
    return get_sum(num-1)+num # 这个是运算逻辑

print(get_sum(6)) # -->21
