# copy 模块里有copy 和 deepcopy 两个函数，分别用来对数据进行深复制和浅复制
import copy
import uuid

nums = [1, 4, 3, 5, 6, [100, 200, 300], 6, 7]
nums1 = copy.copy(nums)  # 对nums列表进行浅复制
nums2 = copy.deepcopy(nums)  # 对nums列表进行深复制
print("copy", nums1)
print("deepcopy", nums2)


# uuid模块 用来生成一个全局唯一的id

print(uuid.uuid1())  # 长度32，每一个字符有16个选择 ==> 所以重复可能性是16**32之一
# uuid1 是基于MAC地址，时间戳，随机数来生成唯一的uuid
# 所以保证整个系统是唯一的id
# 生成的id是随机的

# print(uuid.uuid2()) # uuid2 由于算法的原因python是不支持这个的

# 需要两个参数 namespace 和 字符串, uuid3 生成固定的uuid
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'zhangsan'))
# uuid5和uuid3不是随机的，是根据传入的字符串和指定算法得出的，是固定的
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'zhangsan'))
# uuid3用的算法是 md5 而 uuid5用的是 sha1

print(uuid.uuid4())  # 随机生成，使用最多，通过伪随机得到的uuid，有一定概率重复
