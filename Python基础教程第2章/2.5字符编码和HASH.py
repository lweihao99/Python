# 字符编码, ASCII
# 每个十进制数字代表着一个字符,可以看字符编码表

# 查看字符所对应的ASCII码
# 97 对应 'a'
print(ord("a"))
# 65 对应 'A'
print(ord("A"))


# HASH, 一般翻译为散列，杂凑或者哈希，是将任意长度的输入通过HASH算法变换成固定长度的输出，而这个输出就是散列值.
# 这种转换是一种压缩映射，也就是hash值得空间通常远小于输入的空间，
# 比如一个电影有1Gb,通过hash转化之后只有20byte,这20byte 代表的不是电影本身，你不能通过20byte直接看电影，而是你可以通过这20byte找到电影原文件，一种联系
# 比如我设计一个最简单的数字算法， 输入+7=输出 ---> 比如我输入1，输出就变成了8; 输入2,输出就变成了9, 而hash 要更复杂
# hash 算法不过是一个更为复杂的运算，它的输入可以使字符串，可以是数据，可以是任何文件，经过hash运算后变成一个固定长度的输出，该输出就是 hash 值.
# hash算法有个特点，就是你不能从结果推算出输入，所以又称为不可逆的算法
# 比如 hello ---> 1228478748，从输出你推断不出输入，但是从输入可以推断出输出，因为 hello 对应 1228478748，但是要注意的是,这个值每次重启程序都会变
print(hash("hello"))

# hash 的另一个特效是计算速度极快，比如一个 20Gb 的电影和一个 5Kb 文件复杂度相同,计算量都极小,都可以在0.1秒之内得出结果

# hash 能做什么?
# 1、密码,基于hash的md5加密算法 保证同样的输入得出的结果一直一致

# 2、文件完整性校验
# 比如 20gb ----> asdqqwdasd, 而下次还是对应这个基于hash值, md5值
# 所以可以给一个文件赋值,然后要是下载下来的文件对应这个 md5值，那就说明你下载的这个文件是对的，是完整的

# 3、数字签名
# 你 A -----> B 其他人, B不知道 A 被 C 给替换了，C模仿A 发给 B假情报， B为了验证真实性，就需要对个暗号，如果对不上就说明这个情报是假的
# 而用在互联网里，同理，也需要商议一个暗号，就是 私钥（用来加密的）;把文件进行hash,生成一段hash 值（就是所谓的'摘要信息'）,然后将这段摘要信息进行加密，因为原文是加密不了的
# A 将原文 + 加密信息一同发给 B; B 有公钥，就是用来解密的,然后得到 hash 值 --> B 对原文进行hash --> B 拿这个hash值跟 A 发过来的进行比较,如果一致代表情报发送者就是A本人


# 基于hash的数据类型
# dict--> 特点:key 唯一,key 不可变, 查询速度块,且不受dict 大小影响. dict 的 key 是都要经过hash运算的,所以是唯一和不可变,只有不可变的数据可以 hash
# dict 查询速度快的原因是, dict 里的每个 key 都要生成一个固定的hash值,然后将每个不同的hash值存放到一个列表里,
# 所以当我们要查找某个 key的时候,会将key 先hash,得到hash值,然后在拿这个值,到之前存放每个key的hash值得列表里去找,使用二分法来找,所以速度会很快
# 当然 dict真正的查询算法是比上面要复杂很多,但是查询速度快的基本逻辑是不差的

# set
# 集合天生去重的原理是因为每存一个值到set里的时候，都要先经过hash，然后根据得出的hash值算出，这个值应该存放到set的那个位置，
# 而每次存放的时候都会检查要存放的位置有没有值，有的话就对比是否相等，如果相等，则不在存储新值，如果不相等(即为空)，则把新值存放进去
