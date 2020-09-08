import hashlib
import hmac

# 这两个模块都是用来进行数据加密的

# hashlib 模块里主要支持两个算法 md5 和 sha 加密模块
# 加密方式有： 单向加密-->md5/sha ， 对称加密-->， 非对称加密-->rsa
# 单向加密只有加密的过程，不能解密

# 需要将要加密的内容转化为二进制
x = hashlib.md5()  # 生成一个md5 对象
# x = hashlib.md5('abc'.encode())
x.update('abc'.encode('utf-8'))  # 加密
print(x.hexdigest())  # 900150983cd24fb0d6963f7d28e17f72
# abc ==> 900150983cd24fb0d6963f7d28e17f72
# 不能通过算法反推成abc，但是abc每次都是900150983cd24fb0d6963f7d28e17f72


# 文件的md5讲解看 python 教程 2020 版 1-10.16 hashlib 和 hmac 模块

# hashlib 其他加密方法,sha比起md5更安全, 比如 sha224
h1 = hashlib.sha1('12345'.encode())
print(h1.hexdigest())

# 224 代表位数， 一个16进制占4位，所以长度是56位==> 56*4=224
h2 = hashlib.sha224('123456'.encode())
print(h2.hexdigest())

h3 = hashlib.sha256('12345'.encode())
print(h3.hexdigest())

h4 = hashlib.sha384('12345'.encode())
print(h4.hexdigest)


# hmac 加密可以对指定秘钥
h = hmac.new('h'.encode(), '你好'.encode())
result = h.hexdigest()
