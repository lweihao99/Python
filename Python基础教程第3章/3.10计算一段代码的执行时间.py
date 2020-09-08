import time # time模块可以获取当前的时间
# 代码运行之前，获取一下时间

# 为了避免重复的写代码，写计算执行时间的代码，可以使用函数
def calc_time(fn):

    start = time.time() # time模块里的time方法，可以获取当前时间的时间戳
    # 时间戳是从 1970-01-01 00:00:00 UTC 到现在的秒数
    #
    print('start=',start)

    fn()
    # x = 1

    # for i in range(1,100000): # 将这段代码封装成函数参数
    #     x *= i
    # print(x)

    # 代码运行完成以后，在获取一下时间
    end = time.time()

    print('代码运行耗时{}秒'.format(end - start))

def demo():
    x = 1

    for i in range(1,100000): # 将这段代码封装成函数参数
        x *= i
    print(x)

def foo():
    start = time.time()
    # 模拟
    print('hello')
    time.sleep(3)
    print('world')
    end = time.time()
    print('代码运行耗时{}'.format(end - start))



calc_time(demo) # 这里不能加括号因为要传参
calc_time(foo)




# y = 1

# for j in range(1,10000):
#     y*=j
# print(y)

# start = time.time()
# # 模拟
# print('hello')
# time.sleep(3)
# print('world')
# end = time.time()
# print('代码运行耗时{}'.format(end - start))