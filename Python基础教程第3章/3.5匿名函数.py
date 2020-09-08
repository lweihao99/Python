# 在python中普通函数是使用def关键字来定义，而匿名函数就是没有名字的函数，就是没有函数名，匿名函数是使用lambda关键字来创建的
''' lambda 的语法:
lambda 参数1，参数2，参数3:执行代码语句(执行代码表达式)
在 lambda 之后的参数可以是无数个:这里是表达式
特点：
    1，使用lambda关键字去创建函数
    2，没有函数，而def后面则需要创建一个函数名
    3，匿名函数冒号后面的表达式有且只有一个，注意：是表达式，而不是执行语句
    4，匿名函数自带一个return，而这个return的结果就是表达式计算后的结果
缺点:
    1，lambda只能是单个表达式，不能是代码块，他的设计就是为了满足简单函数的场景，只能封装有限的逻辑
    复杂逻辑实现不了，必须使用def来处理
'''
# 使用lambda表达式来计算两个数的和:
test =lambda x,y: x+y # 这里是同通过一个变量来接受lambda，然后通过变量来调用函数
test(1,3) # 给参数赋值分别对应x和y
print(test(4,5)) # 由于匿名函数自带return所以返回值会直接返回到调用函数上

calc = lambda a,b,c:a*b*c
print(calc(2,3,10))
age = 15
print("可以参军" if age>18 else "继续上学") # 三元运算看1.8


# 在匿名函数里使用三元运算
funcTest = (lambda x,y:x if x>y else y)(13,16) # 后面可以直接写参数数值,可以直接调用
print(funcTest)

f = (lambda x:(x**2)+810)(10)
print(f)


# 而转化成普通函数就是
def test(x,y):
    return x+y

print(test(3,4))
# 可以将函数名赋值给另一变量，使这个变量指向同一个内存地址，就是存储了函数代码的内存地址(指向了同一个对象)
# 所以匿名函数没有名字可以赋值一个变量名
new =test # 给函数名起另一名
print(new(3,5))


# 简单的实例
# 函数的一种用法，回调函数，将函数当做其他函数的参数
def calc(a,b,fn):
    # fn这个参数是为了避免重复的改变函数里的内容,重复调用其他函数
    # 这种方法可以自如的选择自己想要的算法结果比如要加法就输出变量 x1
    # 想要减法就输出变量 x2
    return fn(a,b) # 调用add函数,在将add函数的返回值返回给变量 x,调用函数的算法

# def add(x,y):
#     return x+y

# def minus(x,y):
#     return x-y

# x1 = calc(1,2,add)
# print(x1)
# x2 = calc(10,5,minus)
# print(x2)

# 使用匿名函数来当参数
x1 = calc(10,5,lambda x,y:x+y) # 将lambda函数当做参数来给函数使用里面的算法
x2 = calc(20,25,lambda x,y:x-y) # lambda 的 x,y 对应 fn(a,b)里的 a,b
x3 = calc(10,10,lambda x,y:x*y)
x4 = calc(100,10,lambda x,y:x/y)
print(x1,x2,x3,x4)

