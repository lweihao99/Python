import time
# 使用装饰器对代码进行优化

def calc_time(fn):
    def inner(x,*args,**kwargs):
        start = time.time()
        s = fn(x) # 将x值传给demo的实参
        end = time.time()
        print('代码耗时',end-start)
        return s # 这里要是不返回，在调用的时候输出值为None
    
    return inner


@calc_time # @之后写外部函数，这是装饰器的语法糖，原理:第一件事是调用外部函数,第二件事是将函数demo传给fn，也就是被装饰的函数传递给fn
def demo(n):
    x = 1

    for i in range(1,n): # 将这段代码封装成函数参数
        x *= i
    return x

# @calc_time # 装饰器
# def foo():
#     # 模拟
#     print('hello')
#     time.sleep(3)
#     print('world')


m = demo(100000,'good',s='hello') # 调用inner返回值 # 由于是调用inner所以参数是给到inner的 # 对原有的函数进行参数扩充
print('m=',m)
# foo()