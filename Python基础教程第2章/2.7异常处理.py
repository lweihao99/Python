# 当一个文件出现错误将会导致程序终止运行

# 异常捕获
# try:
#     print("-----test--------1")
#     f = open("text.txt", "r")  # 这一行会报错，打开了一个不存在的文件,发生异常
#     print("-----test-------2----")
#     print(name)  # 这是 NameError

# # except 后面的错误得和产生的错误相匹配
# # 异常类型想要被捕获, except 后面的错误得相匹配
# except (IOError, NameError) as rusult:  # except 表示可能出现的错误, 而文件找不到属于 IO 异常(输入输出异常)
#     print("产生错误")  # 捕获异常后执行代码
#     print(result)
#     pass


# 异常捕获要将所有可能出现的错误写进 except() 的括号里
# as 变量名--->是将错误信息打印出来
# 异常的统一名字，可以捕获所有异常就是只用 Exception
# try:
#     print("-----test--------1")
#     f = open("text.txt", "r")  # 这一行会报错，打开了一个不存在的文件,发生异常
#     print("-----test-------2----")
#     print(name)  # 这是 NameError

# # except 后面的错误得和产生的错误相匹配
# # 异常类型想要被捕获, except 后面的错误得相匹配
# except Exception as rusult:  # except 表示可能出现的错误, 而文件找不到属于 IO 异常(输入输出异常)
#     print("产生错误")  # 捕获异常后执行代码
#     print(result)
#     pass

import time
# try....finally 和嵌套
try:
    f = open("text.txt", "r")
    # try 可以嵌套
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            # 2 秒休息时间,需要time模块
            time.sleep(2)
            print(content)

    # finally 是一定会被执行的，哪怕之前由于错误程序中断了
    finally:
        f.close()
        print("文件关闭")

except Exception as result:
    print("发生异常")
