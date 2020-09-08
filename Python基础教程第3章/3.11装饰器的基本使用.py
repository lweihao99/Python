import time
# 使用装饰器对代码进行优化

def calc_time(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('代码耗时',end-start)
    
    return inner


@calc_time # @之后写外部函数，这是装饰器的语法糖，原理:第一件事是调用外部函数,第二件事是将函数demo传给fn，也就是被装饰的函数传递给fn
def demo():
    x = 1

    for i in range(1,100000): # 将这段代码封装成函数参数
        x *= i
    print(x)

@calc_time
def foo():
    # 模拟
    print('hello')
    time.sleep(3)
    print('world')
    

# 第三件事是当在次调用demo函数时，demo函数已经不再是上面的demo，而是inner的返回值
demo()
foo()