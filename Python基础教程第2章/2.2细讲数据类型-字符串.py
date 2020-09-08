# 字符串：一个有序的字符集合
# 字符串的特性：
# 1、字符串按照从左到右的顺序定义字符集合
# 2、字符串也有下标，下标从0开始顺序访问，有序
# 3、可以进行切片操作
# 4、字符串是不可变的，不能像列表一样修改其中某个元素，所有对字符串的修改操作其实都是相当于生成了一份新数据

# 注:字符串的单引号和双引号都无法取消特殊字符的含义，如果想让引号内所有字符均取消特殊含义，需要在引号前面加 r
# 比如： names = r "l\n\tf"

name = "weihao"
# 打印 w
print(name[0])
# 切片，打印 weih
print(name[0:4:1])
# 索引
print(name.index("w"))  # 返回 0

# 字符串的常用操作
a = "weihao"
print(a.capitalize())  # .capitilize 首字母大写
a.casefold()  # .casefold 字符串全变小写

print(a.center(100, "-"))  # 将 a 的字符串放到中间 .center(长度，补充)

# 计数，算字符个数, 语法：.count(sub,star,end), star 默认是0，end默认是-1,， start 和 end 可以不写 默认 0,-1
a.count("w", 0, -1)

# .endswith 判断字符串以什么字符串为结尾,并且返回 True or False
print(a.endswith("ao"))
# .starswith 判断字符串以什么字符从开始

# .find 查找字符下标
a.find("a")  # 可以规定查找范围 start,end ，默认是0,-1
# .index 同列表的用法
a.index("i")  # 查找 "i" 的下标


# .format 格式化
s = "My name is %s, i'm %s years old" % ("weihao", 21)  # 格式化,具体看 第一章 1.4
# 第二种格式化方法
ss = "Hello, my name is {0}, and im {1} years old, {0} your welcome,{2}"
# 打印 Hello, my name is weihao, and im 21 years old, weihao your welcome,bye
print(ss.format("weihao", 21, "bye"))
# .format 另一种写法
ss1 = "Hello {name}, welcome to {city} , where {friend_name} is living"
# 打印 Hello Weihao, welcome to Milano , where Paolo is living
print(ss1.format(name="Weihao", city="Milano", friend_name="Paolo"))

# .isdigit() 判断是不是整数,返回 True or False
n = "4\t"
print(n.isdigit())
# .islower() 查看字符串是不是全部小写,返回布尔类型
print(ss1.islower())
# .isupper() 判断字符串是不是全部大写
print(ss1.isupper())
# .isspace() 判断是不是空格
print("是不是空格:", ' '.isspace())

# .join 拼接，将列表或者元组里的数据拼接成字符串,只能拼接字符串,同时列表将转化成字符串
w = ";"
q = ["1", "2", "3", "4"]
print(w.join(q))  # '1;2;3;4'
qq = w.join(q)
# .ljust 左对齐，不足的部分用你想要的字符补全,列表或元组不能使用
print(qq.ljust(50, "+"))
# .rjust 右对齐

# .lower 将字符串里所有大写字母换成小写
print(ss1.lower())
# .upper 将字符串全部大写
ss1.upper()

# .strip 删除所有空格
z = "\n \t hello \t \n"
print(z.strip())
# .lstrip , .rstrip 删除左右空格
print(z.rstrip())  # 右
print(z.lstrip())  # 左

# .replace 替换字符串
score = "my score is 400, not very good"
print(score.replace("400", "600", 1))  # count 是要改的次数，默认为1

# .split 将字符串变成列表，然后区分,方便操作或者提取元素
print(qq.split(","))  # .split(sep,maxsplit), sep 是区分,比如如果字符串里有 ","就以 ","来区分元素
# 因为.split默认是转化成一整个列表所以，如果字符串里包含了多个元素就可以用 sep 区分成多个元素
# maxsplit 是一共区分几次，如果不写就默认全区分
# .rsplit 从右开始区分

# .swapcase 将大写换成小写，小写换成大写
score.swapcase()

# .zfill 自定一个长度，如果字符串长度不够就用0来填充
a = "weihao"
print(a.zfill(20))  # 长度20
