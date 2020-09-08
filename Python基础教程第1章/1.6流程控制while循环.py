import random
# while 循环
# 语法是 while 条件为真: 执行代码
count = 0  # 计数器
while count < 10:  # 循环100次你好，由于count 永远都是 0 所以会进入死循环
    print("你好", count)
    count += 1  # 为了避免死循环，就让 count 每循环一次就+1一直到99为止

count1 = 0
while count1 <= 10:
    print("hello world")  # 循环十次 hello world
    count1 += 1

# 打印 0 到 100 之间的偶数
count2 = 0
while count2 < 10:
    if count2 % 2 == 0:  # 如果除以2 的余数是0 就是偶数
        print("这是偶数", count2)
    count2 += 1

# 猜随机数字
n = random.randint(0, 10)
count3 = 5  # 能猜的次数
while count3 > 0:
    # 每次循环都猜一个数字,所以得在循环下面，要是在循环外面就是输入一个数字之后就没了并且循环你这个数字所对应的答案
    enter = int(input("enter your number:"))
    if enter > n:
        print("try smaller")
    elif enter < n:
        print("bigger")
    else:
        print("great,you got it!!")
        break  # 终止循环 ， exit()是程序退出
        # continue 类似于 break 是终止单次循环
    count3 -= 1
print(n)

# continue 使用演示
count4 = 0
while count4 < 20:
    count += 1
    if count4 > 8 and count4 < 12:
        continue  # 终止单次循环，这里就是不运行 8 到 12 之间的循环
    print(count4)
else:  # while 后面跟一个else 的作用是 当循环正常结束时执行，正常结束就是循环没有被 break 或者 exit() 终止时执行
    print("hello!")
# break 和 continue 只能在循环中使用
# 死循环 dead loop  就是让条件一直为真
while True:  # 注意 True 大小写
    print("你是风儿我是沙")
# 死循环可以用到监控上，比如每几个星期监控一次，程序永远运行
