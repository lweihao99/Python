# 实现文件拷贝功能  比如 xxx.txt ==> xxx.bak.txt , bak= backup 就是备份文件
import os

file_name = input('请输入一个文件路径:')

if os.path.isfile(file_name):  # 判断是否是文件，文件是否存在
    # 为了避免读取非文本文文件的时候报错，以rb二进制的方式读取,不用解码
    old_file = open(file_name, 'rb')  # 转化文字为编码,就是每个汉字对应的utf-8编码

    # 将旧文件的数据读取出来，再写入到新的文件
    # 需要根据输入的名字生成,比如 xxx + bak + txt
    # names = file_name.rpartition('.')  # 使用 . 分隔,从右边切片 ==> 结果是一个元祖 ('xxx','.','txt')
    # new_file_name = names[0]+'.bak.'+names[2]  # 拼接成 xxx.bak.txt

    # 可以使用os模块的方法,splitext
    names = os.path.splitext(file_name)  # 一个元祖 ('xxx','.txt'), 这个是从最后一个 . 开始切
    new_file_name = names[0]+'.bak'+names[1]

    # 以二进制的形式读取，就以二进制的形式写入,结果是一样的,在写入的时候会自动用utf-8的方式转换二进制为可读文字
    # 打开新文件用于写入,想要手动转换的话可以使用 decode('utf8') 从新解码
    new_file = open(new_file_name, 'wb')
    while True:
        content = old_file.read(1024)  # 节省电脑资源，提高效率,指定每次读取1024字节
        new_file.write(content)
        if not content:
            break

    new_file.close()
    old_file.close()
else:
    print('你输入的文件不存在')
