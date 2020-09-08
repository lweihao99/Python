names = input("输入你的名字:")  # 储存用户输入的数据
age = int(input("输入你的年龄:"))  # 转化input 字符串成 int整数
height = float(input("输入你的身高:"))  # 转化成 float小数 浮点数

# 美化文本输出
msg = '''
--------Personal info---------
Name  : %s 
Age   : %d
Height: %f
-------------END--------------

''' % (names, age, height)  # 将我要加入的信息写进去
# 为了让 各个信息打印在他需要去的位置 就要用到站位符 %s 按 %()里的顺序打印, %s s代表 string 字符串, 如果想要输出的必须是数字(整数)的话就是 %d 代表 digital,
# 如果用的 input 输入的话 所有输入的数据都会以 字符串处理 所以这时候用 %d 就会报错 如果要转化成数字类型的话就 int(input("age"))
# 如果想打印出浮点数 就要用 %f float
# %r 就是替换成 raw 原生字符
print(msg)  # 打印出用户输入的数据
if height <= "180":
    print("你好矮啊！")
