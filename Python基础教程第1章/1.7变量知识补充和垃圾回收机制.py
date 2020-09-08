# 如何查看内存地址
name = "weihao"
print(id(name))  # 打印内存地址

name = "jone"
# 内存地址改了, 由于 name 变量 跟 weihao 的联系断了，内存地址改了，没有编号了，所以就找不到 weihao 这个储存在内存里的字符串了
print(id(name))
# Python 每隔一段时间会检查内存里是否有无用数据，没有内存地址的（和变量名没有关联的），如果有就会将之回收

# 变量指向

name = "weihao"

name1 = name  # 给name1 赋值 另一个变量 ---> name1 = "weihao"
print(name1)  # 打印 weihao
print(id(name), id(name1))  # 内存地址一样

name = "jojo"
print(name)  # 变量名的值改了,在一个新的内存地址创建新的值

print(name1)  # 还是会打印 weihao 而不是打印新的变量名
# name1 指向的不是 name， 而是name 的内存地址给了 name1,
# 然后 name1 直接指向 "weihao"， 所以哪怕name 的值改了， name1 还是会打印 "weihao" ,
# name 和 name1 不是直接联系的
